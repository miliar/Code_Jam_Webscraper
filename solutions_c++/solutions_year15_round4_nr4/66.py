//*
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <functional>
#define MOD 1000000007
#define MAX ((1<<30)-1)
#define MAX2 ((1ll<<62)-1)
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef set<int>::iterator siit;

ll d[200][2];

int r, c;

ll mul_inv(ll a, ll b)
{
	ll b0 = b, t, q;
	ll x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

int main()
{
	int t, tt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tt);
	for(t=0;t<tt;t++)
	{
		int i, j, k;
		ll dab=0;
		memset(d, 0, sizeof(d));
		scanf("%d%d", &r, &c);
		if(c%12 == 0)
		{
			ll rot1, rot3, rot4, rot6, rot12;
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
			}
			rot1=d[r][0]+d[r][1];
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 2) d[i][1]+=d[i-2][0]*3;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot3=d[r][0]+d[r][1];
			rot3-=rot1;
			rot3*=mul_inv(3, MOD);
			rot3%=MOD;
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 3) d[i][1]+=d[i-3][0]*4;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot4=d[r][0]+d[r][1];
			rot4-=rot1;
			rot4*=mul_inv(4, MOD);
			rot4%=MOD;
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 2) d[i][1]+=d[i-2][0]*3;
				if(i >= 2) d[i][1]+=d[i-2][0]*6;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot6=d[r][0]+d[r][1];
			rot6-=rot1;
			rot6-=rot3*3;
			rot6*=mul_inv(6, MOD);
			rot6%=MOD;
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 2) d[i][1]+=d[i-2][0]*3;
				if(i >= 3) d[i][1]+=d[i-3][0]*4;
				if(i >= 2) d[i][1]+=d[i-2][0]*6;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot12=d[r][0]+d[r][1];
			rot12-=rot1;
			rot12-=rot3*3;
			rot12-=rot4*4;
			rot12-=rot6*6;
			rot12*=mul_inv(12, MOD);
			rot12%=MOD;
			dab=rot1+rot3+rot4+rot6+rot12;
		}
		else if(c%6 == 0)
		{
			ll rot1, rot3, rot6;
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
			}
			rot1=d[r][0]+d[r][1];
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 2) d[i][1]+=d[i-2][0]*3;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot3=d[r][0]+d[r][1];
			rot3-=rot1;
			rot3*=mul_inv(3, MOD);
			rot3%=MOD;
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 2) d[i][1]+=d[i-2][0]*3;
				if(i >= 2) d[i][1]+=d[i-2][0]*6;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot6=d[r][0]+d[r][1];
			rot6-=rot1;
			rot6-=rot3*3;
			rot6*=mul_inv(6, MOD);
			rot6%=MOD;
			dab=rot1+rot3+rot6;
		}
		else if(c%4 == 0)
		{
			ll rot1, rot4;
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
			}
			rot1=d[r][0]+d[r][1];
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 3) d[i][1]+=d[i-3][0]*4;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot4=d[r][0]+d[r][1];
			rot4-=rot1;
			rot4*=mul_inv(4, MOD);
			rot4%=MOD;
			dab=rot1+rot4;
		}
		else if(c%3 == 0)
		{
			//1-rot
			ll rot1, rot3;
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
			}
			rot1=d[r][0]+d[r][1];
			memset(d, 0, sizeof(d));
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
				if(i >= 2) d[i][1]+=d[i-2][0]*3;
				d[i][0]%=MOD, d[i][1]%=MOD;
			}
			rot3=d[r][0]+d[r][1];
			rot3-=rot1;
			rot3*=mul_inv(3, MOD);
			rot3%=MOD;
			dab=rot1+rot3;
		}
		else
		{
			d[0][0]=d[0][1]=1;
			for(i=1;i<=r;i++)
			{
				if(i >= 2) d[i][0]+=d[i-2][1];
				if(i >= 1) d[i][1]+=d[i-1][0];
			}
			dab=d[r][0]+d[r][1];
		}
		printf("Case #%d: %I64d\n", t+1, (dab%MOD+MOD)%MOD);
	}
	return 0;
}
//*/