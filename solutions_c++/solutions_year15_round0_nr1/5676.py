#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
using namespace std;
int main(){
	FILE *fp, *ofp;
	//fopen_s(&fp, "A-small-attempt.in", "r"), fopen_s(&ofp, "yungshunchang.out", "w");
	freopen_s(&fp, "A-large.in", "r", stdin);
	freopen_s(&ofp, "output.out", "w", stdout);
	//freopen_s(&ofp, "output.out", "w", stdout);
	int T = 0;
	//scanf_s("%d", &T);
	cin >> T;
	for (int k = 0; k < T; k++){
		int Smax;
		cin >> Smax;
		//scanf_s("%d", &Smax);
		char S[1010];
		int S2[1010];
		//scanf_s("%s", &S);
		cin >> S;
		int sum = 0, min_inv = 0;
		for (int i = 0; i < Smax; i++){
			S2[i] = S[i] - 48;
		}
		for (int j = 0; j < Smax + 1; j++){
			if (sum < j) {
				min_inv += j - sum;
				sum = j;
			}
			sum += S2[j];
		}
		printf("Case #%d: %d\n", k + 1, min_inv);
	}
	return 0;
}