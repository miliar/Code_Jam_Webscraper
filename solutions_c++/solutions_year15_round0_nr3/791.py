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
const int N = 10005;
int sign[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 1, 1, 1},
	{0, 1, -1, 1, -1},
	{0, 1, -1, -1, 1},
	{0, 1, 1, -1, -1}
};
int nxtv[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, 1, 4, 3},
	{0, 3, 4, 1, 2},
	{0, 4, 3, 2, 1}
};
char orig[N];
int L, val[N];
LL X;
pair<int, int> getAns(pair<int, int> x, pair<int, int> y)
{
	pair<int, int> ret;
	ret.first = x.first * y.first * sign[x.second][y.second];
	ret.second = nxtv[x.second][y.second];
	return ret;
}
int getLeftLength()
{
	pair<int, int> cur = make_pair(1, 1);
	for(int i = 1; i <= 4; i++)
	{
		for(int j = 0; j < L; j++)
		{
			cur = getAns(cur, make_pair(1, val[j]));
			if(cur == make_pair(1, 2))
				return (i - 1) * L + j + 1;
		}
	}
	return -1;
}
int getRightLength()
{
	pair<int, int> cur = make_pair(1, 1);
	for(int i = 1; i <= 4; i++)
	{
		for(int j = L - 1; j >= 0; j--)
		{
			cur = getAns(make_pair(1, val[j]), cur);
			if(cur == make_pair(1, 4))
				return (i - 1) * L + L - j;
		}
	}
	return -1;
}
int checkAll()
{
	pair<int, int> part = make_pair(1, 1);
	for(int i = 0; i < L; i++)
		part = getAns(part, make_pair(1, val[i]));
	pair<int, int> ret = make_pair(1, 1);
	for(int i = 1; i <= X % 4; i++)
		ret = getAns(ret, part);
	return ret == make_pair(-1, 1);
}
int main()
{
	int t, cas = 1;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%lld", &L, &X);
		scanf("%s", orig);
		for(int i = 0; i < L; i++)
			val[i] = orig[i] - 'i' + 2;
		int left = getLeftLength();
		int right = getRightLength();
		printf("Case #%d: ", cas++);
		if(left == -1 || right == -1 || left + right >= X * L || !checkAll())
			printf("NO\n");
		else
			printf("YES\n");	
	}
    return 0;
}
