//============================================================================
// Name        : code.cpp
// Author      : vlade087
// Version     : 1.0
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<sstream>
#include<math.h>
#include<ctype.h>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<algorithm>
#include <complex>
#include <numeric>
#include<list>
#include<deque>
#include <stdlib.h>
#define mod 1000000007
#define inf 200000000000000L
#define countbits __builtin_popcount
#define sz sizeof
#define mp make_pair
#define pb push_back
#define ll long long
#define ull unsigned long long
#define mset memset
#define sz sizeof
#define maxn 2000000
#define EPS 1e-9
#define par pair<int,int>
using namespace std;
int n,m,k,x,y,tt;
bool use[20],use1[20];
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&tt);
	for(int w = 1; w<=tt;w++)
	{
		scanf("%d",&n);
		mset(use,0,sz(use));
		mset(use1,0,sz(use1));
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				scanf("%d",&x);
				if(i == n)
				{
					use[x]=1;
				}
			}
		}
		scanf("%d",&n);
		for(int i=1;i<5;i++)
			for(int j=1;j<5;j++)
			{
				scanf("%d",&x);
				if(i == n)
				{
					use1[x]=1;
				}
			}
		m = 0;
		k = 0;
		for(int i=1;i<17;i++)
			if(use[i] && use1[i])
			{
				m = i;
				k++;
			}
		printf("Case #%d: ",w);
		if(k == 0)
		{
			printf("Volunteer cheated!\n");
		}else if(k == 1	)
		{
			printf("%d\n",m);
		}else
			printf("Bad magician!\n");
	}
	return 0;
}
