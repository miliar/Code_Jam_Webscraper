#include <cstring>
#include <iostream>
#include <stdio.h>
#include <cmath>

#define TAM (10000 + 7)

using namespace std;

int multiply(int a, int b) {
	/*
	i = 2
	j = 3
	k = 4

		1	i	j	k
	1	1	i	j	k
	i	i	-1	k	-j
	j	j	-k	-1	i
	k	k	j	-i	-1

		1	2	3	4
	1	1	2	3	4
	2	2	-1	4	-3
	3	3	-4	-1	2
	4	4	3	-2	-1
	*/

	bool change_symbol = a*b < 0;

	int val = -1;

	a = abs(a);
	b = abs(b);

	if(a == 1)
		val = b;
	else if(b == 1)
		val = a;

	else {

		if(a == b)
			val = -1;

		// row 2
		else if(a == 2) {
			if(b == 3)
				val = 4;
			else if(b == 4)
				val = -3;
		}
		// row 3
		else if(a == 3) {
			if(b == 2)
				val = -4;
			else if(b == 4)
				val = 2;
		}
		// row 4
		else if(a == 4) {
			if(b == 2)
				val = 3;
			else if(b == 3)
				val = -2;
		}
	}

	if(change_symbol)
		val = -val;

	return val;
}

int data[TAM];
bool possible_k[TAM];
char text[TAM];

int main() {
	int T, L, X;
	char c;

	scanf("%d", &T);
	for(int test=1; test<= T;test++) {
		scanf("%d%d", &L, &X);
		
		scanf("%s", text);
		for(int i = 0;i < L;i++) {

			int val = text[i] - 'j' + 3;
			for(int j = 0; j < X;j++)
				data[L*j + i] = val;
		}

		bool possible = false;

		int _len = L*X;

		int poss_k = 1;
		for(int i = _len-1;i >= 0;i--) {
			poss_k = multiply(data[i], poss_k);
			possible_k[i] = poss_k == 4;
		}

		int looking_for_i = 1;

		for(int i = 0; i < _len && !possible;i++) {
			looking_for_i = multiply(looking_for_i, data[i]);

			// is 'i'
			if(looking_for_i == 2) {
				int looking_for_j = 1;

				for(int j = i+1;j < _len  && !possible;j++) {
					looking_for_j = multiply(looking_for_j, data[j]);

					// is 'j'
					if(looking_for_j == 3) {
						// is 'k'
						possible = possible_k[j+1];}
				}
			}
		}

		printf("Case #%d: %s\n", test, possible ? "YES": "NO") ;
	}
	return 0;
}
