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
int p , r , s;
string a[100] , b[100];
int u[100];

int main()
{
	freopen("D-small-attempt1.in" , "r" , stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for (test = 1; test <= t; test++)
	{
		cin>>n;
		for (i = 0; i < n; i++)
			cin>>a[i];
		
		
		int tot = n * n;
		int ans = 1000;
		for (k = 0; k < (1<<tot); k++)
		{
			int sum = 0;
			for (j = 0; j < n; j++)
				b[j] = a[j];
			for (j = 0; j < tot; j++)
			{
				if (k & (1<<j))
				{
					int x = j / n;
					int y = j % n;
					if (a[x][y] == '0')
						sum++;
					b[x][y] = '1';
				}
			}

			if (k == 15)
				k = k;
			int good = 1;
			for (i = 0; i < n; i++)
				u[i] = 0;
			for (i = 0; i < n; i++)
			{
				int cnt = 0;
				for (j = 0; j < n; j++)
				{
					if (b[i][j] == '1')
					{
						u[j] = 1;
						cnt++;
					}
				}
				if (cnt == 0)
					good = 0;
				int tot = 0;
				for (j = 0; j < n; j++)
				{
					if (b[j] == b[i])
						tot++;
				}

				if (tot != cnt)
					good = 0;
			}

			for (i = 0 ;i < n; i++)
				if (!u[i])
					good = 0;
			if (good)
				ans = min(ans , sum);
		}

		cout<<"Case #"<<test<<": "<<ans<<endl;;
		
	}

	return 0;
}