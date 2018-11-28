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

using namespace std;

ll n, i, j, k, m;
int u[10];

int main() 
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin >> n;
		for (i = 0; i < 10; i++)
			u[i] = 0;

		cout << "Case #" << tt << ": ";

		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
		}
		else
		{
			set<int> s;
			ll k = n;
			while (s.size() < 10)
			{
				ll tmp = k;
				while (tmp)
				{
					s.insert(tmp % 10);
					tmp /= 10;
				}

				k += n;
			}
			cout << k - n << endl;
		}
	}
	return 0;
}