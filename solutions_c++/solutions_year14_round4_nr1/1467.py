// GCJ2014R2.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

#pragma warning(disable:4996)

using namespace std;

int N,C;
int sp[11000];
bool flag[11000];

void init()
{

}

int solve()
{
	int ret = 0;

	sort(sp, sp+N);
	int j=N-1;
	for (int i=0; i<N; i++) {

		if (j>i) {
			while (j>i && sp[j] + sp[i] > C) {
				j--;
			}
			if (j>i) {
				ret++;
				j--;
			}
		}
	}
	return N - ret;
}

void work()
{
	int T;

	scanf("%d", &T);
	for (int ca=1; ca<=T; ca++)
	{
		scanf("%d%d", &N, &C);
		for (int i=0; i<N; i++) {
			scanf("%d", &sp[i]);
		}
				
		cout << "Case #" << ca << ": ";		
		int ret = solve();
		cout << ret << endl;		
	}
}


int main()
{
	freopen("C:\\Users\\yuazh\\Downloads\\A--large.in", "r", stdin);
	freopen("C:\\Users\\yuazh\\Downloads\\A--large.out", "w", stdout);
	init();
	work();

	return 0;
}

