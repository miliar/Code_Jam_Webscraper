#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
#include <deque>
#include <stack>
#include <stdio.h>
#include <map>
#include <set>
#include <time.h>
#include <string>
#include <fstream>
#include <queue>
#include <bitset>
#include <cstdlib>
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pdd pair<double,double>
#define pii pair<ll,ll>
#define PI 3.14159265358979323846
#define MOD 1000000007
#define MOD2 1000000009
#define INF (1LL+(ll)1e+15)
#define x1 fldgjdflgjhrthrl
#define x2 fldgjdflgrtyrtyjl
#define y1 fldggfhfghjdflgjl
#define y2 ffgfldgjdflgjl
#define N 100500
#define mx 112
#define sqval 1000
#define eps 1e-9
#define BLACK 0
#define WHITE 1
#define MAG 1000
typedef long long ll;
typedef long double ld;
using namespace std;
ll n,m,i,j,k,kk,l,r,x,y,z,ans;
ld a[100500], dp1[15], dp2[15];
vector <ll> f;
string norm(string s, ll y)
{
	ll sz = (1<<y);
	for (int i = 0; i < y; i++)
	{
		for (j = 0; j < sz; j+=(1<<(i+1)))
		{
			string t1,t2;
			for (k = j; k < j+(1<<i); k++)
				t1.push_back(s[k]);
			for (k = j+(1<<i); k < j+(1<<(i+1)); k++)
				t2.push_back(s[k]);
			if (t1 > t2)
			   for (k = j; k < j+(1<<i); k++)
				   swap(s[k], s[k+(1<<i)]);
		}
	}
	return s;
}
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		printf("Case #%d: ", ii+1);
		cin >> n >> kk;
		for (i = 0; i < n; i++)
			cin >> a[i];
		ld ans = 0;
		f.clear();
		for (i = 0; i < (1<<n); i++)
		{
			ll bits = 0;
			for (j = 0; j < n; j++)
				if ((i&(1<<j))!=0)
				   bits++;
			if (bits == kk/2)
			   f.push_back(i);
		}
		ll sz = f.size();
		for (i = 0; i < sz; i++)
			for (k = i+1; k < sz; k++)
				if ((f[i]&f[k]) == 0)
				{
					ll x = f[i];
					ll y = f[k];
					for (j = 0; j <= kk/2; j++)
						dp1[j] = dp2[j] = 0;
					dp1[0] = dp2[0] = 1;
					for (j = 0; j < n; j++)
						if ((x&(1<<j)) != 0)
						{
							for (l = kk/2-1; l >= 0; l--)
							{
								dp1[l+1] += dp1[l]*a[j];
								dp1[l] -= dp1[l]*a[j];
							}
						}
					for (j = 0; j < n; j++)
						if ((y&(1<<j)) != 0)
						{
							for (l = kk/2-1; l >= 0; l--)
							{
								dp2[l+1] += dp2[l]*(1-a[j]);
								dp2[l] -= dp2[l]*(1-a[j]);
							}
						}
					ld tmp = 0;
					for (j = 0; j <= kk/2; j++)
						tmp += dp1[j]*dp2[j];
					 ans = max(ans, tmp);
				}
		printf("%.9f\n",(double)ans);
	}
	return 0;
}
