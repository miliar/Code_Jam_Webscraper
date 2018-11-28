#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
double Naomi[1001];
double Ken[1001];
int N;

int compare (const void * a, const void * b)
{
	return ( (*(double*)a > *(double*)b) - (*(double*)a < *(double*)b) );
}

int deWar(double *naomi, double *ken, int n)
{
	int i = 0, j = 0, l = n-1;
	int count = 0;
	int count2 = 0;
	while (i < n && j < l+1) {
		while (naomi[i] <= ken[j] && i < n) { i++; count2++;}
		if (i != n) {
			count++;
			l = l - count2;
		}
		i++; j++;
		count2 = 0;
	}
	return count;
}

int War(double *naomi, double *ken, int n)
{
	int i = 0, j = 0;
	int count = 0;
	while(i < n && j < n) {
		while (naomi[i] >= ken[j] && j < n) {j++;}
		count++;
		if (j == n)
			count--;
		i++;
		j++;
	}
	return n - count;
}

int main() {
	int Te;
	scanf("%d", &Te);
	for (int Ti = 1; Ti <= Te; Ti++) {
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> Naomi[i];
		Naomi[N] = 1;
		for (int i = 0; i < N; i++)
			cin >> Ken[i];
		Ken[N] = 1;

		qsort(Naomi, N, sizeof(double), compare);/*
		FOR(i, 0, N)
			cout << Naomi[i] << " ";
		cout << endl;*/

		qsort(Ken, N, sizeof(double), compare);/*
		FOR(i, 0, N)
			cout << Ken[i] << " ";
		cout << endl;*/

		int dw = deWar(Naomi, Ken, N);
		int w = War(Naomi, Ken, N);
		printf("Case #%d: %d %d\n", Ti, dw, w);
	}
	return 0;
}
