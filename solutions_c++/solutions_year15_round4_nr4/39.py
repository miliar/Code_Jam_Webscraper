#include<cstdio>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

const ll mod = 1000000007;

const int perioda[5] = {1, 1, 3, 4, 6}, vyska[5] = {1,2,2,3,2}, cislo[5] = {2,3,1,1,1}, moze[4][4] = 
{{0,0,0,0},
{0,0,0,1},
{0,0,0,1},
{0,1,1,0}};

const int nemozna[13] = {1,0,1,0,0,1,0,1,1,1,1,1,0};

int gcd(int a, int b)
{
	if(b == 0)return a;
	return gcd(b, a%b);
}

int lcm(int a, int b)
{
	return a*b/gcd(a,b);
}

ll solve(int r, int c)
{
	vector<vector<vector<ll> > > dp(13, vector<vector<ll> > (4, vector<ll> (r+1, 0)));
	for(int i=0; i<5; i++)
	{
		if(c % perioda[i] == 0 && r >= vyska[i])
		{
			dp[perioda[i]][cislo[i]][vyska[i]] = 1;
		}
	}
	for(int i=1; i<=r; i++)
	{
		for(int j=0; j<5; j++)
		{
			if(c % perioda[j] == 0 && i > vyska[j])
			{
				for(int pp=1; pp<=12; pp++)
				{
					if(nemozna[pp])continue;
					int np = lcm(pp, perioda[j]);
					for(int pc = 1; pc <= 3; pc++)
					{
						dp[np][cislo[j]][i] += dp[pp][pc][i-vyska[j]] * gcd(pp, perioda[j]) * moze[pc][cislo[j]];
						dp[np][cislo[j]][i] %= mod;
					}
				}
			}
		}
	}
	ll res = 0;
	
	/*for(int i=1; i<4; i++)
	{
		for(int j=1; j<=r; j++)
		{
			printf("%lld\t",dp[3][i][j]);
		}
		printf("\n");
	}*/
	
	for(int i=1; i<4; i++)
	{
		for(int j=0; j<=12; j++)
		{
			//printf("%lld\t",dp[j][i][r]);
			res += dp[j][i][r];
			res %= mod;
		}
		//printf("\n");
	}
	return res;
}


int main()
{
	int t;
	scanf("%d",&t);
	for(int test=0; test<t; test++)
	{
		int r,c;
		scanf("%d %d",&r,&c);
		ll res = solve(r,c);
		printf("Case #%d: %lld\n",test+1, res);
	}
	return 0;
}