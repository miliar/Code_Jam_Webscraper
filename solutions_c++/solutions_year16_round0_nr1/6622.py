#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cctype>

#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<set>
#include<algorithm>
#include<stack>
#include<list>

//#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define INF 0x7fffffff
#define ll long long
#define eps 1e-8
#define PI 2*cos(0.0)
#define MOD 1000000007

#define MAXN 1005

ll n;
set<int>s;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-out.out", "w", stdout);
	int T;
	ll tmp1, tmp2;
	cin >> T;
	for (int kase = 1; kase <= T;kase++)
	{
		s.clear();
		cin >> n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", kase);
			continue;
		}
		tmp1 = tmp2 = n;
		while (s.size() != 10)
		{
			while (tmp1)
			{
				s.insert(tmp1 % 10);
				tmp1 /= 10;
			}
			tmp2 += n;
			tmp1 = tmp2;
		}
		tmp2 -= n;
		printf("Case #%d: %lld\n", kase, tmp2);
	}
}