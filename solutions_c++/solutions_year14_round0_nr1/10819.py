#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <queue>
#include <math.h>
#include <string>
#include <memory.h>

using namespace std;
typedef unsigned long long LL;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for ( int k = 0; k < t; k ++)
	{
		int r;
		cin >> r;
		vector<int> p1;
		for ( int i = 0; i < 4; i ++)
		{
			for ( int j = 0; j < 4; j ++)
			{
				int v;
				cin >> v;
				if ( i == r - 1)
					p1.push_back(v);
			}
		}

		cin >> r;
		vector<int> p2;
		for ( int i = 0; i < 4; i ++)
		{
			for ( int j = 0; j < 4; j ++)
			{
				int v;
				cin >> v;
				if ( i == r - 1)
					p2.push_back(v);
			}
		}
		int cnt = 0;
		int val = -1;
		for ( int i = 0; i < 4; i ++)
			for ( int j = 0; j < 4; j ++)
			{
				if ( p1[i] == p2[j])
					cnt++ , val = p1[i];
			}
			cout << "Case #" << k +1 << ": ";
			if ( cnt == 1)
			{
				cout << val << endl;
			}
			else if ( cnt == 0)
			{
				cout << "Volunteer cheated!" << endl;
			}
			else
			{
				cout << "Bad magician!" << endl;
			}
	}
	return 0;
}