#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>

#define INF 2147483647
#define PI acos(-1.0)

using namespace std;

int GO[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
map<char, int> M = {{'^', 0}, {'>', 1}, {'v', 2}, {'<', 3}};

int main(int argc, const char ** argv)
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for(int _t = 1; _t <= tests; ++_t)
	{
		int r, c;
		cin >> r >> c;
		vector <string> A(r);
		for(int i = 0; i < r; ++i)
			cin >> A[i];

		vector <vector <bool> > U(r, vector <bool>(c, false));
		bool impossible = false;
		int res = 0;
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if(!U[i][j])
				{
					if(A[i][j] == '.')
						continue;
					else
					{
						U[i][j] = true;
						int ind = M[A[i][j]];
						int i1 = i + GO[ind][0], j1 = j + GO[ind][1];
						int lasti = i, lastj = j;
						while(i1 >= 0 && i1 < r && j1 >= 0 && j1 < c)
						{
							if(U[i1][j1])
								break;
							if(A[i1][j1] != '.')
							{
								ind = M[A[i1][j1]];
								U[i1][j1] = true;
								lasti = i1, lastj = j1;
							}
							i1 += GO[ind][0], j1 += GO[ind][1];
						}
						if(i1 >= 0 && i1 < r && j1 >= 0 && j1 < c)
							continue;
						bool cur_impossible = true;
						for(int k = 0; k < 4; ++k)
						{
							i1 = lasti + GO[k][0], j1 = lastj + GO[k][1];
							while(i1 >= 0 && i1 < r && j1 >= 0 && j1 < c)
							{
								if(A[i1][j1] != '.')
									break;
								i1 += GO[k][0], j1 += GO[k][1];
							}
							if(i1 >= 0 && i1 < r && j1 >= 0 && j1 < c)
							{
								res++;
								cur_impossible = false;
								break;
							}
						}
						impossible |= cur_impossible;
					}
				}
			}
		}

		if(impossible)
			printf("Case #%d: IMPOSSIBLE\n", _t);
		else
			printf("Case #%d: %d\n", _t, res);
	}

	return 0;
}
