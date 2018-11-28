#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

bool CheckColumn(vector<vector<int> > vec, int value, int c)
{
	for(int i=0;i<vec.size();i++)
		if(vec[i][c] > value) return false;

	return true;
}

bool CheckRow(vector<vector<int> > vec, int value, int r)
{
	for(int i=0;i<vec[r].size();i++)
		if(vec[r][i] > value) return false;

	return true;
}

bool Check(vector<vector<int> > vec, int value, int r, int c)
{
	return CheckRow(vec,value,r) || CheckColumn(vec,value,c);
}

int main() {
	
	ifstream cin("B-small-attempt0.in");
	ofstream cout("output.txt");

	int t;
	cin >> t;

	for(int cs = 1; cs<=t; cs++)
	{
		int r,c;
		cin >> r >> c;

		vector<vector<int> > vec;

		for(int i=0;i<r;i++)
		{
			vector<int> vt;

			for(int j=0;j<c;j++)
			{
				int x;
				cin >> x;
				vt.push_back(x);
			}

			vec.push_back(vt);
		}

		bool can = true;

		for(int i=0;i<vec.size();i++)
		{
			if(can == false) break;

			for(int j=0;j<vec[i].size();j++)
			{
				if(!Check(vec,vec[i][j],i,j))
				{
					can = false;
					break;
				}
			}
		}

		if(can)
		{
			cout << "Case #" << cs << ": YES" << endl;
		}
		else
		{
			cout << "Case #" << cs << ": NO" << endl;
		}
	}

	//system("pause");
	
}
