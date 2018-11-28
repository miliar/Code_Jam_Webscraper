#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;
FILE *stream;

int main()
{
	freopen_s(&stream,"D-large.in","r",stdin);
	freopen_s(&stream,"output.txt","w",stdout);
	int t;
	cin >> t;
	for (int z = 1; z <= t;++z)
	{
		int n;
		cin >> n;
		vector <double> v1(n), v2(n);
		for (int i = 0; i < n; ++i)
			cin >> v1[i];
		for (int i = 0; i < n; ++i)
			cin >> v2[i];
		set <double> s1, s2;
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		int res1 = 0, res2 = 0;
		for (int i = 0; i < n; ++i)
		{
			s1.insert(v1[i]);
			s2.insert(v2[i]);
		}
		for (int i = n - 1; i >= 0; --i)
		{
			set<double>::iterator it = s2.end();
			it--;
			if (*it>v1[i])
			{
				s2.erase(it);
				continue;
			}
			else
			{
				it = s2.upper_bound(0.);
				res1++;
				s2.erase(it);
			}
		}
		for (int i = 0; i < n; ++i)
		{
			set<double>::iterator it = s1.end();
			it--;
			if (*it>v2[i])
			{
				it = s1.upper_bound(v2[i]);
				res2++;
				s1.erase(it);
				continue;
			}
			else
			{
				break;
			}
		}
		cout << "Case #" << z << ": " << res2 << " " << res1 << "\n";
	}
	return 0;
}