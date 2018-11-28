#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

#define vt vector
#define ll long long


int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++)
	{
		int n;
		cin >> n;
		vt<double> a(n), b(n);
		int normal = 0, deceitful = 0;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		for(int i = 0; i < n; i++)
			cin >> b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int i = 0, j = 0;
		while(i < n)
		{
			while(j < n && b[j] < a[i])
				j++;
			if (j == n)
				normal++;
			else
				j++;
			i++;
		}
		sort(b.begin(), b.end(), greater<double>());
		int f, l;
		f = 0;
		l = n-1;
		for(int i = 0; i < n; i++)
		{
			if (b[i] > a[l])
			{
				f++;
			}
			else
			{
				deceitful++;
				l--;
			}
		}
		cout << "Case #" << cases << ": " << deceitful << " " << normal << endl;
	}
	return 0;
}