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
int val[105][4];
// lft = 0, rgt = 1, up = 2, down = 3
int main()
{
	int t, tcase;
	si(t);
	rep(tcase, 1, t)
	{
		int r, c, i, j;
		si(r); si(c);
		rep(i, 0, r - 1)
		{
			val[i][0] = c;
			val[i][1] = -1;
		}
		rep(i, 0, c - 1)
		{
			val[i][2] = r;
			val[i][3] = -1;
		}
		char str[r + 1][c + 1];
		rep(i, 0, r - 1)
			rep(j, 0, c - 1)
				cin>>str[i][j];
		int ans = 0;
		rep(i, 0, r - 1)
		{
			rep(j, 0, c - 1)
			{
				if(str[i][j] != '.')
				{
					val[i][0] = min(val[i][0], j);
					val[i][1] = max(val[i][1], j);
					val[j][2] = min(val[i][2], i);
					val[j][3] = max(val[i][3], i);
				}
			}
		}
		bool corr = true;
		rep(i, 0, r - 1)
		{
			rep(j, 0, c - 1)
			{
				if(str[i][j] != '.')
				{
					bool fnd1, fnd2, fnd3, fnd4;
					if(val[i][1] > j)
						fnd1 = true;
					else
						fnd1 = false;
					if(val[i][0] < j)
						fnd2 = true;
					else
						fnd2 = false;
					if(val[j][3] > i)
						fnd3 = true;
					else
						fnd3 = false;
					if(val[j][2] < i)
						fnd4 = true;
					else
						fnd4 = false;
					if(!(fnd1 || fnd2 || fnd3 || fnd4))
						corr = false;
					else
					{
						if(str[i][j] == '>' && !fnd1)
							ans++;
						if(str[i][j] == '<' && !fnd2)
							ans++;
						if(str[i][j] == 'v' && !fnd3)
							ans++;
						if(str[i][j] == '^' && !fnd4)
							ans++;
					}
				}
			}
		}
		printf("Case #%d: ", tcase);
		if(!corr)
			printf("IMPOSSIBLE\n");
		else
		{
			pi(ans);
			pn;
		}
	}
	return 0;
}