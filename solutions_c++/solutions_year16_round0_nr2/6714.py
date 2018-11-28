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

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int kase = 1; kase <= T;kase++)
	{
		string a;
		cin >> a;
		int cnt = 0;
		int flag = 0;
		int ans = 0;
		for (int i = 0; i < a.length(); i++)
		{
			if (a[i] == '+')
			{
				while (a[i + 1] == '+')
				{
					i++;
				}
			}
			else
			{
				while (a[i + 1] == '-')
				{
					i++;
				}
				cnt++;
				//flag = 1;
			}
		}
		//if (flag)
		{
			if (a[0] == '-')
			{
				ans = 2 * cnt - 1;
			}
			else
			{
				ans = 2 * cnt;
			}
		}
		/*else
		{
			ans = 0;
		}*/
		printf("Case #%d: %d\n", kase, ans);
	}
}