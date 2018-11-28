#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

int Solution()
{
	double c, f, x;
	cin >> c >> f >> x;
	int y = floor(x / c - 2.0 / f - 1);
	double ans = INF;
	for(int i = max(0, y - 5); i < max(1, y + 5); ++i)
	{
		double res = 0.0, speed = 2.0;
		for(int j = 0; j < i; ++j)
		{
			res += c / speed;
			speed += f;
		}
		res += x / speed;
		if(res < ans)
			ans = res;
	}
	printf("%.9lf", ans);
	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
