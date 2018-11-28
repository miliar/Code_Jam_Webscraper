//============================================================================
// Name        : ProblemB.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<stdio.h>
#include<stdlib.h>

int m[101][101];
int maxH[101];
int maxV[101];

int main() {
	bool flag;
	int t;
	int r, c;
	int i, j, k;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		flag = false;
		scanf("%d %d", &r, &c);
		for (j = 0; j < r; j++) {
			maxH[j] = -1;
		}
		for (j = 0; j < c; j++) {
			maxV[j] = -1;
		}
		for (j = 0; j < r; j++) {
			for (k = 0; k < c; k++) {
				scanf("%d", &m[j][k]);
				if (m[j][k] > maxH[j])
					maxH[j] = m[j][k];
				if (m[j][k] > maxV[k])
					maxV[k] = m[j][k];
			}
		}
		for (j = 0; j < r; j++) {
			for (k = 0; k < c; k++) {
				if(m[j][k]<maxH[j]&&m[j][k]<maxV[k]){
					flag=true;
					break;
				}
			}
			if(flag)	break;
		}
		if(flag)	printf("Case #%d: NO\n",i+1);
		else printf("Case #%d: YES\n",i+1);
	}
	return 0;
}
