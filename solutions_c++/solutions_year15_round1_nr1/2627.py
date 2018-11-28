#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int gT;

#define MAX_N	1000

int gn, nums[MAX_N];

int calcA()
{
	int count = 0;
	for(int i=1; i<gn; i++)
		count += max(0, (nums[i-1] - nums[i]));
	return count;
}

int calcB()
{
	int i, count = 0;
	int max_eat = 0;
	for(i=1; i<gn; i++) {
		/*
		if(nums[i] > nums[i-1]) 
			max_eat = max(max_eat, nums[i-1]);
		else
			max_eat = max(max_eat, nums[i-1] - nums[i]);
		*/
		max_eat = max(max_eat, nums[i-1] - nums[i]);
	}

	for(int i=1; i<gn; i++) {
		count += min(max_eat, nums[i-1]);
	}
	return count;
}

void solve()
{
	int i;
	cin >> gn;
	for(i=0; i<gn; i++)
		cin >> nums[i];

	int na = calcA();
	int nb = calcB();	
	printf("Case #%d: %d %d\n", gT, na, nb);
}

int main(int argc, char cargv[])
{
	int n;
	// freopen("01.in", "r", stdin);
	
	scanf("%d", &n);
	for(gT=1; gT<=n; gT++)
	{
		solve();
	}
	return 0;
}
