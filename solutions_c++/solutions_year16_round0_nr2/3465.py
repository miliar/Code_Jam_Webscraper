//Created By Mayur Agarwal :)

#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <algorithm>
#include <map>
#include <iterator>
#include <functional>
#include <stack>
#include <queue>

#define ll long long
#define ind(a) scanf("%d",&a)
#define in(a) scanf("%lld",&a)
#define inc(a) scanf("%c",&a)
#define ins(a) scanf("%s",a)
#define pr(a) printf("%lld\n",a)
#define prc(a) printf("%c",a)
#define prs(a) printf("%s\n",a)
#define fori(I,N) for(ll I=0;I<N;I++)
#define forin(i,n) for(ll I=1;I<=N;I++)
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define ALL(X) (X).begin(), (X).end()
#define pi   acos(-1.0)
#define mod 1000000007
#define SIZE 200010

using namespace std;
typedef pair<ll, ll>pll;
char s[205];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	//ios_base::sync_with_stdio(0); cin.tie(0);
	int t;
	ind(t);
	for (int xx = 1; xx <= t; xx++)
	{
		ins(s);
		int n = strlen(s);
		ll ans = 0;
		for (int i = 1; i < n; i++)
		{
			if (s[i] != s[i - 1])
			{
				ans++;
			}
		}
		if (s[n - 1] == '-')
			ans++;
		cout << "Case #" << xx << ": ";
		cout << ans << endl;
	}
	return 0;
}