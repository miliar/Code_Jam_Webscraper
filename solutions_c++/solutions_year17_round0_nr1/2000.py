#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<utility>
#include<map>
#include<set>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define REP(i,a,b) for(int i=a; i<=b; ++i)
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define MP make_pair
#define sf scanf
#define pf printf
typedef long long LL;
typedef pair<int,int> pii;

const int maxn = 1000;

char arr[maxn+5];

int main()
{
	int T, n, m, ans;
	sf("%d", &T);
	REP(t,1,T)
	{
		sf("%s", arr);
		sf("%d", &m);
		n = strlen(arr), ans = 0;
		for(int i = 0; i+m-1 <= n-1; ++i)
			if(arr[i] == '-')
			{
				++ans;
				for(int k = i; k <= i+m-1; ++k)
					arr[k] = (arr[k] == '+') ? '-' : '+';
			}
		for(int i = max(0, n-m); i <= n-1; ++i)
			if(arr[i] != '+')
				ans = -1;
		printf("Case #%d: ", t);
		if(ans == -1)
			printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
