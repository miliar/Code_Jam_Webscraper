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
ll nums[10005];
int main()
{
	ll i, j, t, n, m, k, l, r, mini, maxi, temp, flag, x, c;
	sc(t);
	fre(i, 1, t)
	{
		sc(x);
		sm(r, c);
		if(x==1)
			printf("Case #%lld: GABRIEL\n", i);
		else if(x==2)
		{
			if((r*c)<x || (r*c)%2==1)
				printf("Case #%lld: RICHARD\n", i);
			else
				printf("Case #%lld: GABRIEL\n", i);
		}
		else if(x==3)
		{
			if((r==3 && c==3) ||(r==3 && c==2) ||(r==2 && c==3) ||(r==4 && c==3) ||(r==3 && c==4))
				printf("Case #%lld: GABRIEL\n", i);
			else
				printf("Case #%lld: RICHARD\n", i);
		}
		else
		{
			if((r==3 && c==4)||(r==4 && c==3) ||(r==4 && c==4))
				printf("Case #%lld: GABRIEL\n", i);
			else
				printf("Case #%lld: RICHARD\n", i);
		}
	}
return 0;
}
