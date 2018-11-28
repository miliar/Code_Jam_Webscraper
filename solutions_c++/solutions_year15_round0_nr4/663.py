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
int main()
{
	int t, tcase;
	si(t);
	rep(tcase, 1, t)
	{
		int x, r, c;
		si(x);
		si(r);
		si(c);
		printf("Case #%d: ", tcase);
		if(x == 1)
			printf("GABRIEL\n");
		else if(x == 2)
		{
			if((r * c) & 1)
				printf("RICHARD\n");
			else
				printf("GABRIEL\n");
		}
		else if(x == 3)
		{
			if(r * c == 6 || r * c == 9 || r * c == 12)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
		else if(x == 4)
		{
			if(r * c >= 12)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
	}
	return 0;
}