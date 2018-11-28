/*
ID: ashish1610
PROG:
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
#define ll				long long int
#define vi				vector<int>
#define vl				vector<ll>
#define	pii				pair<int,int>
#define pil				pair<int, ll>
#define pll				pair<ll, ll>
#define pli 			pair<ll, int>
#define pb(v, a)		v.push_back(a)
#define mp(a, b)		make_pair(a, b)
#define MOD				1000000007
#define rep(i, a, b)	for(i=a; i<=b; ++i)
#define rrep(i, a, b)	for(i=a; i>=b; --i)
#define si(a)			scanf("%d", &a)
#define sl(a)			scanf("%lld", &a)
#define pi(a)			printf("%d", a)
#define pl(a)			printf("%lld", a)
#define pn 				printf("\n")
ll pow_mod(ll a, ll b)
{
	ll res = 1;
	while(b)
	{
		if(b & 1)
			res = (res * a) % MOD;
		a = (a * a) % MOD;
		b >>= 1;
	}
	return res;
}
double v[7000], c[7000];
int main()
{
	int t, tcase;
	si(t);
	rep(tcase, 1, t)
	{
		double V, N, X;
		cin>>N>>V>>X;
		int i;
		rep(i, 1, N)
			cin>>v[i]>>c[i];
		double tm = 0;
		if(N == 1)
		{
			tm = V/v[1];
			if(X != c[1])
				tm = -1;
		}
		else if(N == 2 && c[1] == c[2])
		{
			v[1] += v[2];
			tm = V / v[1];
			if(X != c[1])
				tm = -1;
		}
		else
		{
			double t1, t2;
			t1 = (V / v[1]) * (X - c[2]) / (c[1] - c[2]);
			t2 = (V / v[2]) * (c[1] - X) / (c[1] - c[2]);
			tm = max(t1, t2);
			if(t1 < 0 || t2 < 0)
				tm = -1;
		}
		printf("Case #%d: ", tcase);
		if(tm < 0)
			cout<<"IMPOSSIBLE\n";
		else
			printf("%0.10f\n", tm);
	}
	return 0;
}