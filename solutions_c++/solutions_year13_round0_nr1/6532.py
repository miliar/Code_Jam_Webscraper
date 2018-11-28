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

int main()
{
	int n;
	ifstream cin("input.txt");
	ofstream fout("out.txt");

	cin>>n;
	for(int u = 0; u < n ; u++)
	{
		fout<<"Case #"<<u+1<<": ";
		int xT = -1;
		int yT = -1;
		char arr[4][4];
		bool draw = true;
		for(int i = 0; i < 4; i ++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin>>arr[i][j];
				if(arr[i][j] == 'T')
				{
					xT = i;
					yT = j;
				}
				if(arr[i][j] == '.')
					draw = false;
			}
		}
		bool found = false;
		char T[2] = {'X', 'O'};
		for(int y = 0; y < 2 && !found; y++)
		{
			if(xT != -1)
				arr[xT][yT] = T[y];
			for(int i = 0; i < 4; i ++)
			{
				found = true;
				if(arr[i][0] == '.')
				{
					found = false;
					continue;
				}
				for(int j = 1; j < 4; j++)
				{
					if(arr[i][j] != arr[i][0])
						found = false;
				}
				if(found)
				{
					fout<<arr[i][0]<<" won"<<endl;
					break;
				}
			}
			if(found)
				continue;

			for(int i = 0; i < 4; i ++)
			{
				found = true;
				if(arr[0][i] == '.')
				{
					found = false;
					continue;
				}
				for(int j = 1; j < 4; j++)
				{
					if(arr[j][i] != arr[0][i])
						found = false;
				}
				if(found)
				{
					fout<<arr[0][i]<<" won"<<endl;
					break;
				}
			}
			if(found)
				continue;

			int stX[4] = {0, 0, 3, 3};
			int stY[4] = {0, 3, 0, 3};
			int incX[4] = {1, 1, -1, -1};
			int incY[4] = {1, -1, 1, -1};

			for(int i = 0; i < 4; i ++)
			{
				int x, y;
				string tmp = "";
				for(x = stX[i], y = stY[i]; x >= 0 && y >= 0 && x <4 && y < 4; x += incX[i], y += incY[i])
				{
					tmp += arr[x][y];
				}
				if(tmp == "XXXX" || tmp == "OOOO")
				{
					found = true;
					fout<<tmp[0]<<" won"<<endl;
					break;
				}
			}
			if(found)
				break;

		}
		if(!found && draw)
			fout<<"Draw"<<endl;
		else if (!found)
			fout<<"Game has not completed"<<endl;
	}
	return 0;
}