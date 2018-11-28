#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<queue>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int pp = 1;
	while(T--)
	{
		int d;
		vector<int>v;
		int res = 0;
		scanf("%d", &d);
		for(int i = 0; i < d; i++)
		{
			int x; 
			scanf("%d", &x);
			res = max(res, x);
			v.push_back(x);
		}
		int k = 2;
		while(k < res)
		{
			int cur = 0;
			for(int i = 0; i < v.size(); i++)
			{
				cur += (v[i]-1)/k;
			}
			res = min(res, cur + k);
			k ++;
		}
		printf("Case #%d: %d\n", pp++, res);
	}
}
