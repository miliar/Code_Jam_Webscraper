#define _CRT_SECURE_NO_DEPRECATE
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
using namespace std;

const int MaxN = 1000 + 10;
int T, A[MaxN], N, Ans, big, start, total;

int cmp(const void *a, const void *b){
	return (*(int *)a) - (*(int *)b);
}

int main(){
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d", &N);
		big = 0;
		start = 1;
		for (int j = 1; j <= N; j++){
			scanf("%d", &A[j]);
			if (A[j] > big) big = A[j];
		}
		Ans = big;
		qsort(A + 1, N, sizeof(int), cmp);
		for (int j = 1; j <= big; j++){
			total = 0;
			while (A[start] <= j) start++;
			for (int k = start; k <= N; k++){
				int u = A[k] % j;
				if (u == 0) u = j;
				total += (A[k] - u) / j;
				if (total > Ans) break;
			}
			total += j;
			if (total < Ans) Ans = total;
		}
		printf("Case #%d: %d\n",i, Ans);
	}
	return 0;
}