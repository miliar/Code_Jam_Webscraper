#define _CRT_SECURE_NO_WARNINGS
 
#include <iostream>
#include <functional>
#include <vector>
#include <queue> 
#include <string>
#include <math.h>
#include <algorithm>
#include <limits>
#include <set>
#include <map>
 
#define sqr(x) ((x) * (x))
#define eps 0.00000001
 
using namespace std;

priority_queue <int> q, q2;

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
	int t, n, val[1000], ans, val1, val2;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n;
		for (int j = 0; j < n; j++)
			cin >> val[j];

		int a = 10000;
		for (int q = 1; q <= 1000; q++)
		{
			ans = 0;
			for (int j = 0; j < n; j++)
			{
				if (q <= val[j])
				{
					ans += val[j] / q;
					ans--;
					if (val[j] % q != 0)
						ans++;
				}
			}
			ans += q;
			if (ans < a)
				a = ans;
		}

		cout << "Case #" << i + 1 << ": " << a << endl;
	}
}