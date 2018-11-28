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

int main()
{
	int t;
	ifstream in("B-small-attempt1.in");
	ofstream out("outin.out");
	in >> t;
	int a[100][100],b[100][100];
	for(int cases = 1; cases <= t; cases++)
	{
		int n, m;
		in >> n >> m;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				in >> a[i][j];
				b[i][j] = 100;
			}
		}
		vector<int> hhits(n),vhits(m);
		for(int i=0;i<n;i++)
		{
			int maxh = 0;
			for(int j=0;j<m;j++)
			{
				if(maxh<a[i][j])
					maxh = a[i][j];
			}
			hhits[i] = maxh;
		}
		for(int j=0;j<m;j++)
		{
			int maxh = 0;
			for(int i=0;i<n;i++)
			{
				if(maxh<a[i][j])
					maxh = a[i][j];
			}
			vhits[j] = maxh;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(b[i][j]>hhits[i])
					b[i][j] = hhits[i];
			}
		}

		for(int j=0;j<m;j++)
		{
			for(int i=0;i<n;i++)
			{
				if(b[i][j]>vhits[j])
					b[i][j] = vhits[j];
			}
		}

		bool correct = true;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(b[i][j]!=a[i][j])
					correct = false;
			}
			if(!correct)
				break;
		}
		
		if(correct)
			out << "Case #" << cases << ": " << "YES" << endl;
		else
			out << "Case #" << cases << ": " << "NO" << endl;
	}
	system("pause");
	return 0;
}