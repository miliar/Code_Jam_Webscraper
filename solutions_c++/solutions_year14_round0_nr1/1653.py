#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <sstream>

using namespace std;

int board[4][4];

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		int r1;
		scanf("%d",&r1);
		
		for (int i = 0; i < 4; i += 1)
		{
			for (int j = 0; j < 4; j += 1)
			{
				scanf("%d",&board[i][j]);
			}
		}	

		int r2;
		scanf("%d",&r2);
		
		vector<int> v;
		for (int i = 0; i < 4; i += 1)
		{
			for (int j = 0; j < 4; j += 1)
			{
				int a;
				scanf("%d",&a);
				
				if (i == r2-1)
				{
					for (int k = 0; k < 4; k += 1)
					{
						if (board[r1-1][k] == a)
							v.push_back(a);
					}
				}
			}
		}
		
		printf("Case #%d: ",t);
		
		if (v.empty())
			printf("Volunteer cheated!\n");
		else if (v.size() == 1)
			printf("%d\n",v[0]);
		else
			printf("Bad magician!\n");
	}
	
	return 0;
}
