#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

#define ONE		0
#define I		1
#define J		2
#define K		3
#define mONE	4
#define mI		5
#define mJ		6
#define mK		7

int multT[8][8] = {
		{ONE, I, J, K},
		{I, mONE, K, mJ},
		{J, mK, mONE, I},
		{K, J, mI, mONE}
};

int mult(int a, int b)
{
	int neg = 1;
	if (a > 3) {
		neg *= -1;
		a -= 4;
	}
	if (b > 3) {
		neg *= -1;
		b -= 4;
	}
	if (neg == -1) {
		int result = multT[a][b];
		if (result > 3)
			return result - 4;
		else
			return result + 4;
	}
	else
		return multT[a][b];
}


using namespace std;

int checkis(char* input, int start, int end, int V)
{
	int current = input[start];
	if (current == V)
		return start + 1;
	for (int i = start + 1; i < end; i++) {
		current = mult(current, input[i]);
		if (current == V)
			return i + 1;
	}
	return 0;
}

int checkisK(char* input, int start, int end)
{
	int current = input[start];
	for (int i = start + 1; i < end; i++) {
		current = mult(current, input[i]);
	}
	return current == K;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int L;
		long long X;
		scanf("%d %lld", &L, &X);
		char *input = new char[10001000];
		scanf("%s", input);
		// TODO Deal with base cases
		if (L*X < 3) {
			printf("Case #%d: NO\n", t + 1);
			continue;
		}
		X = ((X - 1) % 256 + 1);
		
		
		for (int i = 0; i < L; i++) {
			if (input[i] == 'i')
				input[i] = I;
			else if (input[i] == 'j')
				input[i] = J;
			else
				input[i] = K;
		}
		for (int i = L; i < L*X; i++)
			input[i] = input[i - L];
		/*
		vector<int> listofI; // stores index of last element needed to make I
		int current = input[0];
		if (current == I)
			listofI.push_back(0);
		for (int i = 1; i < L*X - 2; i++) {
			current = mult(current,input[i]);
			if (current == I)
				listofI.push_back(i);
		}

		vector<int> listofK; // stores index of first element needed to make K
		current = input[L*X-1];
		if (current == K)
			listofK.push_back(L*X - 1);
		for (int i = L*X - 2; i >= 2; i--) {
			current = mult(input[i],current);
			if (current == K)
				listofK.push_back(i);
		}
		bool answer = false;
		for (int a = 0; a < listofI.size(); a++) {
			for (int b = 0; b < listofK.size(); b++) {
				if (listofK[b] - listofI[a] - 1 >= 1) {
					if (checkisJ(input, listofI[a] + 1, listofK[b])) {
						answer = true;
						a = listofI.size();
						break;
					}
				}
			}
		}
		*/
		bool answer = false;
		int jstart = checkis(input, 0, L*X, I);
		int kstart;
		if (jstart) {
			kstart = checkis(input, jstart, L*X, J);
			if (kstart)
				answer = checkisK(input, kstart, L*X);
		}
		if (answer)
			printf("Case #%d: YES\n", t + 1);
		else
			printf("Case #%d: NO\n", t + 1);
	}
	return 0;
}