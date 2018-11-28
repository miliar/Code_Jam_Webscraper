#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <sstream>
using namespace std;

int main(void)
{
	int T;
	cin >> T;

	int mat[4][4][4]; // 0 if richard wins, 1 if gabriel

	for (int x = 0; x < 4; x++)
	for (int r = 0; r < 4; r++)
	for (int c = 0; c < 4; c++)
	{
		mat[x][r][c] = -1;
	}
	mat[2][1][2] = mat[2][2][1] = mat[2][2][2] = mat[2][2][3] = mat[2][3][2] = 1;
	mat[3][2][3] = mat[3][3][2] = mat[3][3][3] = 1;

	for (int x = 0; x < 4; x++)
	for (int r = 0; r < 4; r++)
	for (int c = 0; c < 4; c++)
	{

		if (x == 0) mat[0][r][c] = 1;
		else if (x == 1) mat[1][r][c] = ((r+1)*(c+1))%2 == 0? 1 : 0;
		else if (r == 0 || c == 0) mat[x][r][c] = 0; 
		else if(mat[x][r][c] == -1)
		{
			mat[x][r][c] = 0;
		}
		
	}

	for (int i = 0; i < T; i++)
	{
		int X, R, C;
		cin >> X >> R >> C;
		string res = mat[X-1][R-1][C-1] ? "Gabriel" : "Richard";	
		cout << "Case #" << i+1 << ": " << res << "\n";
	}
	return 0;
}

