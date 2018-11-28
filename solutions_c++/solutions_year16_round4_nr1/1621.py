#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<string>
#include<queue>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

const int MAXN = 100010;

int n;

bool check(int n, int P, int R, int S, string &ans)
{
	if (n==0)
	{
		if (P) ans = "P";
		if (R) ans = "R";
		if (S) ans = "S";
		return 1;
	}
	int s = (P+R+S)/2;
	int a = s - S;
	int b = s - P;
	int c = s - R;
	if (!(0<=a&&a<=s)) return 0;
	if (!(0<=b&&b<=s)) return 0;
	if (!(0<=c&&c<=s)) return 0;
	bool ret = check(n-1, a, b, c, ans);
	if (ret)
	{
		string tmp;
		for (auto x : ans)
		{
			if (x=='P') tmp += "PR";
			if (x=='R') tmp += (n==::n)?"RS":"SR";
			if (x=='S') tmp += (n==::n||n+1==::n)?"PS":"SP";
		}
		ans = tmp;
	}
	return ret;
}

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	scanf("%d", &Test);
	for (int TT=1; TT<=Test; ++TT)
	{
		printf("Case #%d: ", TT);
		int R, P, S;
		scanf("%d%d%d%d", &n, &R, &P, &S);
		string ans;
		if (check(n, P, R, S, ans))
			puts(ans.c_str());
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}
