#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <math.h>

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	scanf("%d", &T);
	
	for (int i = 1; i <= T; i++){
		int num;
		int word;
		scanf("%d", &num);
		scanf("%d", &word);

		if (num == 0){
			printf("Case #%d: 0\n", i);
		}
		else{
			int numP = 0;
			int kaz = 0;
			for (int k = num; k >= 0; k--){
				int digit = word / (int)pow(10, k) % 10;

				int l = num - k;

				while (numP < l){
					numP++;
					kaz++;
				}

				numP += digit;
			}

			printf("Case #%d: %d\n", i, kaz);
		}
	}



	/*
	for (int Case = 1; Case <= Test; Case++){
		int r, chk[17] = { 0 };
		for (int k = 0; k<2; k++){
			scanf("%d", &r);
			for (int i = 1; i <= 4; i++){
				for (int j = 1; j <= 4; j++){
					int x;
					scanf("%d", &x);
					if (i == r) chk[x]++;
				}
			}
		}

		int res, cnt = 0;
		for (int i = 1; i <= 16; i++) if (chk[i] == 2){
			res = i; cnt++;
		}

		printf("Case #%d: ", Case);
		if (cnt == 0) puts("Volunteer cheated!");
		else if (cnt == 1) printf("%d\n", res);
		else puts("Bad magician!");
	}*/

	return 0;
}
