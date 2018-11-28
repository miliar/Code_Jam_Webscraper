/*
 * 1000.cpp
 *
 *  Created on: 2013-12-14
 *      Author: lenovo
 */
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
double Naomi[1100], Ken[1100];
int main() {
	int T, Case = 0;
	scanf("%d", &T);
	int N;
	int i, j, max, min;
	while (T--) {
		Case++;
		scanf("%d", &N);
		for (i = 0; i < N; i++)
			scanf("%lf", &Naomi[i]);
		for (i = 0; i < N; i++)
			scanf("%lf", &Ken[i]);
		sort(Naomi, Naomi + N);
		sort(Ken, Ken + N);
		max = 0;
		min = 0;
		i = j = N - 1;
		for (; j >= 0; j--) {
			if (Naomi[i] > Ken[j]) {
				i--;
				max++;
			}
		}
		i = j = N - 1;
		for (; i >= 0; i--) {
			if (Naomi[i] < Ken[j]) {
				j--;
				min++;
			}
		}
		printf("Case #%d: %d %d\n", Case, max, N - min);
	}
	return 0;
}
