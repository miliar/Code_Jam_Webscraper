#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <functional>
#include <time.h>

using namespace std;
 
#define ll long long
#define mp make_pair

const int MAXN = 400010;

int a[MAXN];

ll EPS = 1743;

map<string, int> m;

int main()
{
     freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0 (1).out", "w", stdout);
	int a, b, c;
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		ll answer = 0;
		cin >> a >> b >> c;
		for (int i = 0; i < a; i++)
		{
			for (int j = 0; j < b; j++)
			{
				int h = i & j;
				if (h < c)
				{
					answer++;
				}
			}
		}
		cout << "Case #" << z << ": " << answer << endl;
	}
}