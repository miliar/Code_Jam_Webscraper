#define _CRT_SECURE_NO_WARNINGS

#define INPUT "B-small-attempt2.in"
#define OUTPUT "output.txt"

#include <iostream>
using namespace std;

int T, t;
int i, j, k;

int B,b, N;
int M[1001];
int copyM[1001];
int nOfCycle;
int lcmOfTotal;
int result;
int LCM(int a, int b);

int main(){
	freopen(OUTPUT, "w+", stdout);
	freopen(INPUT, "r", stdin);

	cin >> T;

	for (t = 0; t < T; t++){
		lcmOfTotal = 1;
		nOfCycle = 0;

		cin >> B;
		cin >> N;

		for (b = 0; b < B; b++){
			cin >> M[b];
			copyM[b] = M[b];
			lcmOfTotal = LCM(lcmOfTotal, M[b]);
		}
		for (b = 0; b < B; b++){
			nOfCycle += lcmOfTotal / M[b];
		}

		N %= nOfCycle;
		if (N == 0)N = nOfCycle;
		if (N <= B){
			result = N;
		}
		else{
			N -= B;
			while (N){
				i = 1000000;
				j = -1;
				for (b = 0; b < B; b++){
					if (copyM[b] < i){
						i = copyM[b];
						j = b;

						if (i == 0)break;
					}
				}

				if (i == 0){
					copyM[j] = M[j];
					result = j+1;
					N--;
					continue;
				}

				for (b = 0; b < B; b++){
					copyM[b] -= i;
				}
			}
		}

		printf("Case #%d: %d\n", t + 1, result);
	}

	return 0;
}

int LCM(int a, int b){
	int c, gcd = a, temp = b;
	for (c = gcd; c; c = gcd%temp, gcd = temp, temp = c);
	return a*b / gcd;
}