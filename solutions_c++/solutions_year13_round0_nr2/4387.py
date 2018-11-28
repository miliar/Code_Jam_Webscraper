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
#include <cstring>
#include <string>
#include <fstream>

using namespace std;

#define maxx(a, b) ((a > b)? a: b)
#define minn(a, b) ((a < b)? a: b)
#define round(a) (int)(a + 0.5)

int get_powers(long long n, int p)
{
    int res = 0;
    for (long long power = p ; power <= n ; power *= p)
        res += n/power;
    return res;
}

int main()
{
	//cout << pr <<endl;
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w" , stdout);

	int T,N,M, ind = 0;
	scanf("%d", &T);
	int b[110][110];
	while(ind++ < T)
	{
		scanf("%d %d", &N, &M);
		for(int i = 0;i < N;i++)
		{
			for(int j = 0;j < M;j++)
			{
				scanf("%d", &b[i][j]);
			}
		}
		// test
		//int x[] = {-1, 0, 1, 0};
		//int y[] = {0 ,-1, 0, 1};
		bool flag = true;
		for(int i = 0;i < N && flag;i++)
		{
			for(int j = 0;j < M && flag;j++)
			{
				int ii = 0;
				for(;ii < N;ii++)
				{
					if(b[ii][j] > b[i][j])
						break;
				}
				int jj = 0;
				for(;jj < M;jj++)
				{
					if(b[i][jj] > b[i][j])
						break;
				}
				if(ii < N && jj < M)
				{
					flag = false;
				}
			}
		}
		if(flag)
		{
			printf("Case #%d: YES\n", ind);
		}
		else
		{
			printf("Case #%d: NO\n", ind);
		}
	}
    return 0;
}
