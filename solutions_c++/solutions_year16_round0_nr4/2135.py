#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define y1 y11
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);

bool w[10];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int iter = 1; iter <= t; iter++)
	{
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << iter << ": ";
		if (s * c < k) cout << "IMPOSSIBLE" << endl;
		else 
		{
			for (int i = 0; c * i < k; i++)
			{
				ll val = 0;
				for (int j = i * c; j < min(k, (i + 1) * c); j++)
				{
					val = (val * (ll)k + j);
				}
				cout << val + 1 << " ";
			}
			cout << endl;
		}
	}
	return 0;
}