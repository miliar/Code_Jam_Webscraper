#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cstdio>
using namespace std;
#define ll long long
#define N 11000000

ll t;
ll a, n;
ll x[100100];

int main()
{
	cin >> t;
	for(int cas = 1; cas <= t; cas ++)
	{
		cin >> a >> n;
		for(int i = 0; i < n; i ++)
			cin >> x[i];
		sort(x, x+n);
		
		ll res = 1000000000;
		ll cnt = 0;
		for(int i = 0; i < n; i ++)
		{
			// cout << i << " " << x[i] << endl;
			if(a > x[i])
			{
				a += x[i];
			}
			else
			{
				res = min(res, cnt+(n-i));
				if(a == 1)
				{
					cnt ++;
					continue;
				}
				while(a <= x[i])
				{
					a = a+(a-1);
					cnt ++;
				}
				a += x[i];
			}
		}
		res = min(res, cnt);
		cout << "Case #" << cas << ": " << res << endl;
	}
	
	return 0;
}

