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

const int N = 1000005;
int ans[N];
int reverse(int val)
{
	int ret = 0;
	while(val)
	{
		ret = ret * 10 + val % 10;
		val /= 10;
	}
	return ret;
}
void preprocess()
{
	memset(ans, -1, sizeof(ans));
	ans[1] = 1;
	queue<int> que;
	que.push(1);
	while(!que.empty())
	{
		int idx = que.front();
		que.pop();
		if(idx + 1 < N && ans[idx + 1] == -1)
		{
			ans[idx + 1] = ans[idx] + 1;
			que.push(idx + 1);
		}
		int rev = reverse(idx);
		if(rev < N && ans[rev] == -1)
		{
			ans[rev] = ans[idx] + 1;
			que.push(rev);
		}
	}
}
int main()
{
	int t, cas = 1;
	preprocess();
	scanf("%d", &t);
	while(t--)
	{
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", cas++, ans[n]);
	}
    return 0;
}
