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

char a[200000];

int main()
{
	int i, j, k, l;
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>TT;
	for(T=1;T<=TT;T++)
	{
		scanf("%s", a);
		int n=strlen(a);
		string s;
		int ans=0;
		for(i=0;i<n;i++)
		{
			if(!s.size()) s.push_back(a[i]);
			else
			{
				if(a[i] == s.back())
				{
					s.pop_back();
					ans+=10;
				}
				else s.push_back(a[i]);
			}
		}
		ans+=s.size()/2*5;
		printf("Case #%d: %d\n", T, ans);
	}
	return 0;
}
//*/