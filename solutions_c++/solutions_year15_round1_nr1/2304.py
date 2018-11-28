#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <map>
#include <set>

using namespace std;


int main()
{
	freopen("D://in.in", "r", stdin);
	freopen ("D://out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		int n;
		cin >> n;
		vector <int> v(n);
		for(int j = 0; j < n; ++j)
		{
			cin >> v[j];
		}

		int ta = 0, tb = 0,d = 0;

		for(int j = 0; j < n-1; ++j)
		{
			if(v[j] - v[j+1] > 0) ta += v[j] - v[j+1], d = max(d, v[j] - v[j+1]);
		}
	
		for(int j = 0; j < n-1; ++j)
		{
			tb += min(d, v[j]);
		}
		cout << "Case #" << i+1 << ": " << ta << " " << tb << endl;
	}
}