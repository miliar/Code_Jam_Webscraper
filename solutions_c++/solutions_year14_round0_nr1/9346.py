// codejam-magic-trick.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

//#define ONLINE
void online(){
#ifdef ONLINE
#else
	#pragma warning(disable:4996)
	freopen("F:\\新的桌面文件\\tmp\\0.txt","r",stdin);
	freopen("F:\\新的桌面文件\\tmp\\1.txt","w",stdout);
#endif
}


int T;
int ans1,ans2;
int arr1[5][5];
int arr2[5][5];

int main() {
	online();

	scanf("%d", &T);
	for (int k=1; k<=T; ++k) {
		scanf("%d", &ans1);
		for (int i=1; i<=4; ++i) {
			for (int j=1; j<=4; ++j) {
				scanf("%d", &arr1[i][j]);
			}
		}
		scanf("%d", &ans2);
		for (int i=1; i<=4; ++i) {
			for (int j=1; j<=4; ++j) {
				scanf("%d", &arr2[i][j]);
			}
		}


		int possible1[4] = {0};
		int possible2[4] = {0};
		for (int j=1; j<=4; ++j) {
			possible1[j-1] = arr1[ans1][j];
			possible2[j-1] = arr2[ans2][j];
		}
		int count = 0;
		int result = 0;
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				if (possible1[i] == possible2[j]) {
					++count;
					result = possible1[i];
				}
			}
		}

		if (count == 0) {
			printf("Case #%d: Volunteer cheated!\n", k);
		} else if (count == 1) {
			printf("Case #%d: %d\n", k, result);
		} else {
			printf("Case #%d: Bad magician!\n", k);
		}



	}




	return 0;
}

