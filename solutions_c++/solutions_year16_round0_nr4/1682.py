#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <functional>

using namespace std;

#define ll long long
#define vt vector
#define mod 1000000007

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ll t;
	scanf("%lld", &t);
	for (ll cases = 1; cases <= t; cases++)
	{
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ", cases);
		for (int i = 1; i <= s; i++)
			printf("%d ", i);
		printf("\n");
	}
	return 0;
}