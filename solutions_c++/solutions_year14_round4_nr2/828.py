#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
using namespace std;

int p[1123];
vector<pair<int,int> > a;
vector<int> num;
int n;
int hash[1123][1123];
bool been[1123][1123];
int co[1123][2];
int been2[1123][2];


bool comp(pair<int,int> a, pair<int,int> b)
{
	return a.second < b.second;
}

int cost(int i, int tp)
{
	if(been2[i][tp])
		return co[i][tp];
	int retv = 0;
	if(tp == 0)
	{
		for(int j = 0; j < p[num[i]]; j++)
			if(a[j].first > num[i])
				retv++;
	}
	else
	{
		for(int j = n-1; j > p[num[i]]; j--)
			if(a[j].first > num[i])
				retv++;
	}
	been2[i][tp] = true;
//	printf("%d %d %d\n", i, tp, retv);
	return co[i][tp] = retv;	
}

int pd(int i, int j)
{
//	printf("%d %d\n", i, j);
	if(i == j)
		return 0;
	if(been[i][j])
		return hash[i][j];
	been[i][j] = true;
	return hash[i][j] = min(pd(i+1, j) + cost(n-(j-i+1), 0), pd(i, j-1) + cost(n-(j-i+1), 1));
}

int
main(void)
{
	int t;
	scanf("%d", &t);
	for(int T = 1; T <= t; T++)
	{
		memset(been2, 0, sizeof(been2));
		memset(been, 0, sizeof(been));
		a.clear();
		num.clear();
		int x, y = 0;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &x);
			a.push_back(pair<int,int> (x,i));
		}
		sort(a.begin(), a.end());
		for(int i = 0; i < n; i++)
			a[i].first = i;
		sort(a.begin(), a.end(), comp);
		for(int i = 0; i < n; i++)
		{
//			printf("%d\n", a[i].first);
			num.push_back(a[i].first);
			p[a[i].first] = i;
		}
		sort(num.begin(), num.end());
		int ans = pd(0, n-1);
		printf("Case #%d: %d\n", T, ans);
	}
}
