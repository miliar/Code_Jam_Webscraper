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
int n,m,k,y,tt;
double c , f ,x;
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&tt);
	for(int w = 1; w<=tt;w++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		double st = 2.0;
		double res = x / st;
		double next = 0.0;
		double sum = 0.0;
		while(1)
		{
			next = c/st + x/(st+f);
			if(res >= next + sum)
			{
				res = next + sum;
			}else break;
			sum = sum + c/st;
			st = st + f;
		}
		printf("Case #%d: %.7lf\n",w,res);
	}
	return 0;
}
