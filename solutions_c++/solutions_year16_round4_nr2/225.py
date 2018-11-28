#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <stdio.h>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define eps 1e-9
#define PI acos(-1.0)
#define ll long long
#define ull unsigned long long
#define f0(i,n) for (i = 0; i < n; i++)
#define MOD 1000000007
using namespace std;
int i, j, n, m, k , t , test;
double p[1000];

double d[300][600];
double solve(vector<double> v)
{
	int i , j;
	int n = v.size();
	for (i = 0; i <= n; i++)
		for (j = 0; j < 500; j++)
			d[i][j] = 0;


	d[0][0 + 250] = 1;
	for (i = 0; i < n; i++)
	{
		for (j = 1; j < 500; j++)
		{
			d[i + 1][j + 1] += d[i][j] * v[i];
			d[i + 1][j - 1] += d[i][j] * (1 - v[i]);
		}
	}

	return d[n][250];
}

int main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for (test = 1; test <= t; test++)
	{
		cin>>n>>k;
		for (i = 0 ;i < n; i++)
			cin>>p[i];
		
		sort(p , p + n);

		double ans = 0;
		for (i = 0; i <= k; i++)
		{
			vector<double> v;
			for (j = 0; j < i; j++)
			{
				v.push_back(p[j]);
			}

			for (j = n - 1; j >= n - (k - i); j--)
				v.push_back(p[j]);

			ans = max(ans , solve(v));

		}
		cout<<"Case #"<<test<<": ";
		printf("%.9lf\n" , ans);
		
	}

	return 0;
}