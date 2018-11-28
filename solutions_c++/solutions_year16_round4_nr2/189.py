//*
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

int n, m;
double a[300];

vector<double> v;

double d[300][300];

double dodo()
{
	int i, j;
	for(i=0;i<=m;i++) for(j=0;j<=m;j++) d[i][j]=0;
	d[0][1]=v[0];
	d[0][0]=1-v[0];
	for(i=1;i<m;i++)
	{
		for(j=0;j<=m;j++) d[i][j]+=d[i-1][j]*(1-v[i]);
		for(j=1;j<=m;j++) d[i][j]+=d[i-1][j-1]*v[i];
	}
	return d[m-1][m/2];
}

int main()
{
	int i, j, k, l;
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>TT;
	for(T=1;T<=TT;T++)
	{
		printf("Case #%d: ", T);
		cin>>n>>m;
		for(i=0;i<n;i++) scanf("%lf", &a[i]);
		sort(a, a+n);
		double ma=0;
		for(i=0;i<=m;i++)
		{
			v.clear();
			for(j=0;j<i;j++) v.push_back(a[j]);
			for(j=n-m+i;j<n;j++) v.push_back(a[j]);
			ma=max(ma, dodo());
		}
		printf("%.20lf\n", ma);
	}
	return 0;
}
//*/