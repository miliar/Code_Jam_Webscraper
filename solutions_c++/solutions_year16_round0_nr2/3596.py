// created by: Prashant Kumar Singh :)
#include<iostream>
#include<algorithm>
#include<utility>
#include<cstring>
#include<string.h>
#include<set>
#include<map>
#include<math.h>
#include<stdio.h>
#include<vector>
#include<functional>
#include<bitset>
#include<iomanip>
#define ll long long
#define gr greater<ll>()
#define pi acos(-1.0)
#define pb push_back
#define MS0(ar) memset(ar,0,sizeof ar)
#define f first
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ind(a) scanf("%d",&a)
#define inf(a) scanf("%lf",&a)
#define inl(a) scanf("%lld",&a)
#define ins(a) scanf("%s",a)
#define pd(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a);
#define bitcnt(x) __builtin_popcountll(x)
using namespace std;
int vis[10];
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
/*#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
#endif
	freopen("output.txt", "w", stdout);*/
	ll t, k = 0, n, ans = 0, plus = 0, minus = 0;
	string s;
	cin >> t;
	while (t--)
	{
		cin >> s;
		plus = 0, minus = 0;
		if (s[0] == '-')
			minus = 1;
		else
			plus = 1;
		for (int i = 1; i < s.length(); i++)
		{
			if (s[i] != s[i - 1])
			{
				if(s[i]=='+')
				plus++;
			   else
				minus++;
			}
		}
		k++;
		//cout << plus << " " << minus << endl;
		if (plus == 0 && minus == 1)
		{
			ans = 1;
		}
		else if (plus == 1 && minus == 0)
		{
			ans = 0;
		}
		else if (s[s.length() - 1] == '+')
		{
			ans = plus + minus - 1;
		}
		else
			ans = plus + minus;
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}