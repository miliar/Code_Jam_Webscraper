#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <queue>
#include <map>
#include <stack>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
#define LL long long
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define MAXN 10000 + 5
#define INF 1e9
#define eps 1e-9
int n;
LL r, t;
int main()
{
#ifdef LOCAL
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	int maxNum;
	LL area;
	scanf("%d", &T);
	for(int ncas = 1; ncas <= T; ncas++)
	{
		scanf("%I64d%I64d", &r, &t);
		maxNum = 1;
		area = 2 * r + 1;
		while(1)
		{
			area = 2 * maxNum * maxNum + 2 * maxNum * r - maxNum;
			if(area > t) break;
			maxNum++;
		}
		printf("Case #%d: %d\n", ncas, maxNum - 1);
	}
	return 0;
}