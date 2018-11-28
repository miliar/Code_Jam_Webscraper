#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 
#include <stack> 
#include <iomanip> 
#include <queue> 
 

using namespace std; 

const string dirs = "<>^v";
const int di[4] = {0, 0, -1, 1};
const int dj[4] = {-1, 1, 0, 0};

char a[111][111];
int n, m;



bool exists(char dir, int i,int j)
{
	int t;
	for(int k = 0;  k< 4; k++)
		if (dir == dirs[k])
			t = k;
			
	i += di[t], j += dj[t];
	while (i >= 0 && j >= 0 && i < n && j < m)
	{
		if (a[i][j] != '.')
			return true;
		i += di[t], j += dj[t];
	}
	return false;
}

int check()
{
	int res = 0;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
		{
			if (a[i][j] != '.') {
				if (!exists(a[i][j], i, j))
				{
					bool flag = false;
					for(int k = 0; k < 4; k++)
						if (dirs[k] != a[i][j])
							flag |= exists(dirs[k], i, j);
					if (flag)
						res++;
					else
						return -1;
				}
			}
		}
	}
	return res;
}

int main(){ 
	ios_base::sync_with_stdio(false); 
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		cerr << test << endl;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> a[i][j];
		cout << "Case #" << test << ": ";
		if (check() == -1 )
			cout << "IMPOSSIBLE" << endl;
		else
			cout << check() 
			<< endl;
	}
	
	
	return 0; 
} 
