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
using namespace std;
int ar[20][20];
int main() {
	//freopen("in.txt","r", stdin);
	//freopen("out.txt","w", stdout);
	int t;
	scanf("%d", &t);
	int c3 = 1;
	while(t--)
	{
		int n, r, c;
		scanf("%d %d %d", &r, &c, &n);
				for(int i = 0; i < 20; i++)
				{
					for(int j = 0; j < 20; j++) ar[i][j] = 0;
				}
		int res = 10000;
		int k = 1;
		for(int i = 0; i < r*c; i++) k *= 2;
		for(int i = 0; i < k; i++)
		{
			int c2 = 0;
			for(int j = 0; j < r*c; j++)
			{
				if(((i >> j) & 1) != 0)
				{
					ar[j/c][j%c] = 1;
					c2++;
				}
			}
			if(c2 == n)
			{
				int r2 = 0;
				for(int i = 0; i < r; i++)
				{
					for(int j = 0; j < c; j++)
					{
						if(ar[i][j] == 1)
						{
							if(i < r-1 && ar[i+1][j] == 1) r2++;
							if(j < c-1 && ar[i][j+1] == 1) r2++;
						}
					}
				}
				res = min(res, r2);
				for(int i = 0; i < r; i++)
				{
					for(int j = 0; j < c; j++) ar[i][j] = 0;
				}
			}
		}
		printf("Case #%d: %d\n", c3, res);
		c3++;
	}
	return 0;
}

