#include <iostream>
#include <stdlib.h>
#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <cmath>
using namespace std;


int main()
{
	freopen("in2.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 
	int t;
	cin >> t;
	for(int step = 1; step <= t; ++step)
	{
		int n, m;
		cin >> n >> m;
		vector<vector<int> > v(n , vector<int> (m));
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				scanf("%d", &v[i][j]);
		vector<int> r(n, 0);
		vector<int> cc(m, 0);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
			{
				r[i] = max(r[i], v[i][j]);
				cc[j] = max(cc[j], v[i][j]);
			}
			bool flag = true;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				if(v[i][j] != min(r[i], cc[j]))
				{
					flag = false;
				}
		printf("Case #%d: ", step);	
		if(flag)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}