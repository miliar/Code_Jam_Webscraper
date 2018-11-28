#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std;
int grid[101][101];
int N, M;
int main() 
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		cin >> N >> M;
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < M; ++j)
				cin >> grid[i][j];
		bool ok = true;
		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < M; ++j)
			{
				bool ok1 = true;
				for(int k = 0; k < M; ++k)
					ok1 &= grid[i][j] >= grid[i][k];
				bool ok2 = true;
				for(int k = 0; k < N; ++k)
					ok2 &= grid[i][j] >= grid[k][j];
				if(!ok1 && !ok2)
				{
					ok = false;
					goto hell;
				}
			}
		}
hell:
		cout << "Case #" << ti << ": " << (ok ? "YES" : "NO") << endl;
	}
}