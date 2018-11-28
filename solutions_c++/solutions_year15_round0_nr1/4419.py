//----------------------JUGNU---------------------------//
#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define vt(a) vector <ll> a
#define st(a) set <ll> a
#define sti(a) set <ll>::iterator a
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%lld",&a)
#define sm(a,b) scanf("%lld%lld", &a, &b)
#define pr(a) printf("%lld\n", a)
#define pm(a,b) printf("%lld %lld\n", a, b)
#define cn(a) cin >> a
#define ct(a) cout << a << endl
#define isset(x,i) ((x>>i)&1)
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
using namespace std;
char s[10000];
int main()
{
	ll i, j, t, n, m, k, l, r, mini, maxi, temp, flag, result;
	sc(t);
	fre(i, 1, t)
	{
		result = 0LL;
		sc(n);
		scanf("%s", s);	
		temp = s[0] - '0';
		fre(j, 1, n)
		{
			if(temp<j)
			{
				result = result - temp + j;
				temp = j;
			}
			temp = temp + s[j] - '0';
		}
		printf("Case #%lld: %lld\n", i, result);
	}
return 0;
}
