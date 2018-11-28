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
#define int64 long long
#define Sort sort

using namespace std;

int ans[20] = {2,1,1,3,2,3,2,2,3,1,1,5,3,3,1,5,6,4,2,19};
int f[6][6];

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);

	int T;
	scanf("%d", &T);
	int t = 0;
	for (int i=2;i<=6;++i)
		for (int j=3;j<=6;++j)
			f[i][j] = ans[t ++];
	for (int ii=0;ii<T;++ii)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		printf("Case #%d: %d\n", ii + 1, f[n][m]);
	}

	return 0;
}