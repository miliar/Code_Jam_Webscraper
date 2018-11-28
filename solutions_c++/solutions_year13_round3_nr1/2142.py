//============================================================================
// Name        : B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string.h>
using namespace std;

char a[1000002];
int c[1000002];
int pos[1000002], v[1000002];

int main() {

	int sum = 0;
	int t, n;
	int np;
	int len;
	int i, j, k;
	int count;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		sum = 0;
		scanf("%s %d", a, &n);

		len = strlen(a);
		np = 0;
		count = 0;
		for (j = 0; j <= len - n; j++) {
			count = 0;
			for(k=j;k<len;k++){
				if (a[k] != 'a' && a[k] != 'e' && a[k] != 'i' && a[k] != 'o'
									&& a[k] != 'u')
					count++;
				else	count = 0;
				if (count >= n){
					sum+=len-k;
					break;

				}
			}

		}
		printf("Case #%d: %d\n", i + 1, sum);
	}

	return 0;
}

