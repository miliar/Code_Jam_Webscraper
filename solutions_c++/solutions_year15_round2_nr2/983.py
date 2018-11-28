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
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}

int bitCount(int mask)
{
	int ret = 0;
	while(mask)
	{
		mask &= (mask - 1);
		ret++;
	}
	return ret;
}
int check(pair<int, int> x, pair<int, int> y)
{
	return abs(x.first - y.first) + abs(x.second - y.second) == 1;
}
int main()
{
	int cas = 1, t;
	scanf("%d", &t);
	while(t--)
	{
		int R, C, K;
		scanf("%d%d%d", &R, &C, &K);
		int n = R * C, ans = INF;
		for(int i = 0; i < (1 << n); i++)
		{
			if(bitCount(i) == K)
			{
				int cnt = 0;
				vector< pair<int, int> > pts;
				for(int j = 0; j < n; j++)
					if((1 << j) & i)
						pts.push_back(make_pair(j / C, j % C));
				for(int j = 0; j < pts.size(); j++)
					for(int k = j + 1; k < pts.size(); k++)
						if(check(pts[j], pts[k]))
							cnt++;
				checkMin(ans, cnt);
			}
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
    return 0;
}
