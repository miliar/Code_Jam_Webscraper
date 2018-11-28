#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

bool stones[25][25];
bool enclosed[25][25];
int n, m, k;

void ff(int r, int c)
{
	if(r<0 || r>=n || c<0 || c>=m)
		return;
	if(stones[r][c])
		return;
	if(!enclosed[r][c])
		return;
	enclosed[r][c] = false;
	ff(r-1, c);
	ff(r+1, c);
	ff(r, c-1);
	ff(r, c+1);
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		cin >> n >> m >> k;
		int s = n*m;
		int best = s;
		for(int b = 0; b < (1<<s); b++)
		{
			int numstones = 0;
			memset(stones, false, sizeof(stones));
			for(int i=0; i<s; i++)
				if(b & (1<<i))
				{
					int r = i/m;
					int c = i%m;
					stones[r][c] = true;
					numstones++;
				}
			memset(enclosed, true, sizeof(enclosed));
			for(int r=0;r<n;r++)
			{
				ff(r, 0);
				ff(r, m-1);
			}
			for(int c=0;c<m;c++)
			{
				ff(0, c);
				ff(n-1, c);
			}
			int count = 0;
			for(int r=0;r<n;r++)
				for(int c=0;c<m;c++)
					count += enclosed[r][c];

			if(count >= k)
				best = min(best, numstones);
		}
		printf("Case #%d: %d\n", test_case, best);
	}
	return 0;
}
