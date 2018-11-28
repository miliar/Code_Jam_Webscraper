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

const int N = 105;
int val[N];
int main()
{
	int t, cas = 1;
	scanf("%d", &t);
	while(t--)
	{
		int C, D, V;
		scanf("%d%d%d\n", &C, &D, &V);
		for(int i = 1; i <= D; i++)
			scanf("%d", &val[i]);
		sort(val + 1, val + 1 + D);
		int index = 1, ans = 0;
		LL cur = 0;
		while(cur < V)
		{
			if(index > D || cur + 1 < val[index])
			{
				ans++;
				cur += (cur + 1) * C;
			}
			else
				cur += (LL)val[index++] * C;
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
    return 0;
}
