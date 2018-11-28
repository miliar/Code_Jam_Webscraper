#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
	freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int j = 0; j < t; ++j)
	{
		int r,c;
		cin>>r>>c;
		vector<string> map(r);
		for (int i = 0; i < r; ++i)
			cin>>map[i];
		vector<int> rows(r);
		vector<int> cols(c);
		for (int i = 0; i < r; ++i)
		{
			for (int k = 0; k < c; ++k)
			{
				if (map[i][k]!='.')
				{
					++ rows[i];
					++ cols[k];
				}
			}
		}
		int count = 0;
		for (int i = 0; i < r; ++i)
		{
			if (count < 0) break;
			switch (map[i][0])
			{
			case '<': 
				++count;
				if (rows[i] == 1 && cols[0] == 1) count = -1;				
				break;
			case '.': 
				for (int k = 1; k < c; ++k) 
				{
					if (map[i][k] != '.') 
					{
						if (map[i][k] == '<')
							++count;
						if (rows[i] == 1 && cols[k] == 1) count = -1;
						break;
					}
				}
				break;
			}
			if (count < 0) break;
			switch (map[i][c - 1])
			{
			case '>': 
				++count;
				if (rows[i] == 1 && cols[c - 1] == 1) count = -1;	
				break;
			case '.': 
				for (int k = c - 2; k > -1; --k) 
				{
					if (map[i][k] != '.') 
					{
						if (map[i][k] == '>')
							++count;
						if (rows[i] == 1 && cols[k] == 1) count = -1;
						break;
					}
				}
				break;
			}				
		}
		for (int i = 0; i < c; ++i)
		{
			if (count < 0) break;
			switch (map[0][i])
			{
			case '^': 
				++count;
				if (cols[i] == 1 && rows[0] == 1) count = -1;
				break;
			case '.': 
				for (int k = 1; k < r; ++k) 
				{
					if (map[k][i] != '.') 
					{
						if (map[k][i] == '^')
							++count;
						if (rows[k] == 1 && cols[i] == 1) count = -1;
						break;
					}
				}
				break;
			}
			if (count < 0) break;
			switch (map[r - 1][i])
			{
			case 'v': 
				++count;
				if (cols[i] == 1 && rows[r - 1] == 1) count = -1;
				break;
			case '.': 
				for (int k = r - 2; k > -1; --k) 
				{
					if (map[k][i] != '.') 
					{
						if (map[k][i] == 'v')
							++count;
						if (rows[k] == 1 && cols[i] == 1) count = -1;
						break;
					}
				}
				break;
			}
				
		}
		cout<<"Case #" << j + 1 <<": ";
		if (count >= 0)
			cout<<count<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
    return 0;
}
