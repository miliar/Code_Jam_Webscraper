//g++ -std=c++0x your_file.cpp -o your_program
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<set>
#define fname "A-large"
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

const int maxn = 1111;

char s[maxn];

int main()
{
	freopen (fname".in", "r", stdin);
	freopen (fname".out", "w", stdout);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		printf("Case #%d: ", Case);
		int n;
		scanf("%d ", &n);
		gets(s);
		int cur = 0, x, ans = 0;
		for (int i = 0; i <= n; i++)
		{
			int x = (int)s[i] - '0';
			if (x && cur < i)
				ans += (i - cur), cur = i;
			cur += x;
		}
		printf("%d\n", ans);
	}
	return 0;
}
