#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>

using namespace std;

const int N = 4;
const int M = 4;
int s[N][M];
int e[N][M];

int main()
{
	int i, j;
	int n;
	int fst, scd;

	scanf("%d ", &n);	
	for (int l=0; l<n; l++) {

		scanf("%d ", &fst);	
		for (i=0; i<N; i++)
			for (j=0; j<M; j++)
				scanf("%d ", &(s[i][j]));
		scanf("%d ", &scd);	
		for (i=0; i<N; i++)
			for (j=0; j<M; j++)
				scanf("%d ", &(e[i][j]));

		int res = 0;
		int ansC = 0;
		for (i=0; i<M; i++) {
			for (j=0; j<M; j++) {
				if (s[fst - 1][i]	== e[scd - 1][j]) {
					ansC = s[fst - 1][i];
					res++;
					break;
				}
			}
		}

		printf("Case #%d: ", l+1);
		if (res == 0)
			printf("Volunteer cheated!\n");
		else if (res == 1)
			printf("%d\n", ansC);
		else if (res > 1)
			printf("Bad magician!\n");

/*
	printf("%d\n", fst);	
	for (i=0; i<N; i++) {
		for (j=0; j<M; j++)
			printf("%d ", s[i][j]);
		puts("");
	}
	printf("%d\n", scd);	
	for (i=0; i<N; i++) {
		for (j=0; j<M; j++)
			printf("%d ", e[i][j]);
		puts("");
	}
*/

	}



	return 0;
}

