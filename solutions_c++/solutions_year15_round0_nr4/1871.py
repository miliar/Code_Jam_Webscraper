#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

#define mp make_pair


int main()
{
	ios::sync_with_stdio(false);

	bool mat[5][5][5];

	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++)
			for (int k = 0; k < 5; k++)
				mat[i][j][k] = false;


	mat[2][1][2] = mat[2][1][4] = true; 
	mat[2][2][2] = mat[2][2][3] = mat[2][2][4] = true;
	mat[2][3][4] = true; 
	mat[2][4][4] = true;

	mat[3][2][3] = true;
	mat[3][3][3] = mat[3][3][4] =  true;
	
	mat[4][3][4] = true; 
	mat[4][4][4] = true;


	int TC;
	cin >> TC;

	for (int cases = 1; cases <= TC; cases++)
	{

		int X, r, c;
		cin >> X >> r >> c;

		int R = min(r,c), C = max(r,c);

		string ans;
		if(X == 1)
			ans = "GABRIEL";
		else
		{
			if(mat[X][R][C])
				ans = "GABRIEL";
			else
				ans = "RICHARD";
		}

		cout << "Case #" << cases << ": ";
		cout << ans << "\n";
	}
	
	return 0;
}