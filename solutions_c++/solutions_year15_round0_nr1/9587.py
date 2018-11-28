#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		int mx; char a[1000 + 10];
		scanf("%d%s", &mx, a);
		int count = a[0] - '0', need = 0;
		for (int i = 1; i <= mx; i++) {
			if (count < i) need += i - count, count += a[i] - '0' + i - count;
			else count += a[i] - '0';
		}
		printf("Case #%d: %d\n", tc, need);
	}

}