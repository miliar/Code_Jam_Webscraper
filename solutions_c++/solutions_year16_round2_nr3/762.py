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
#define INF (1LL+(ll)1e+9)
#define x1 fldgjdflgjhrthrl
#define x2 fldgjdflgrtyrtyjl
#define y1 fldggfhfghjdflgjl
#define y2 ffgfldgjdflgjl
#define SQ 500400
#define CI 43534
#define N 228228
#define eps 1e-9
typedef long long ll;
typedef long double ld;
using namespace std;
ll n, k,j,i,m,q,ii,timer,x1,x,y,l,nodes_sz;
ll a[1005][1005], a1[1005], a2[1005];
pii b[1005];
ll ans[50];
string s[1005], t[1005];
map<string, ll> ss, tt;
map<string,ll>::iterator itr;
ll Abs(ll x)
{
	return x>0?x:-x;
}
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		cin >> n;
		printf("Case #%d: ",ii+1);
		ss.clear();
		tt.clear();
		for (i = 0; i < n; i++)
		{
			cin >> s[i] >> t[i];
			ss[s[i]] = 0;
			tt[t[i]] = 0;
		}
		i = 0;
		for (itr = ss.begin(); itr != ss.end(); itr++)
		{
			ss[(*itr).X] = i++;
		}
		x = i;
		i = 0;
		for (itr = tt.begin(); itr != tt.end(); itr++)
		{
			tt[(*itr).X] = i++;
		}
		y = i;
		for (i = 0; i < x; i++)
			for (j = 0; j < y; j++)
				a[i][j] = 0;
		ll ans = 0;
		for (i = 0; i < n; i++)
		{
			b[i] = mp(ss[s[i]], tt[t[i]]);
			a[ss[s[i]]][tt[t[i]]] = 1;
		}
		sort(b, b+n);
		for (i = 0; i < (1<<n); i++)
		{
			for (j = 0; j < x; j++)
				a1[j] = 0;
			for (j = 0; j < y; j++)
				a2[j] = 0;
			ll bits = 0, k = 0;
			for (j = 0; j < n; j++)
			if ((i&(1<<j)) != 0)
			{
				bits++;
				if (!a1[b[j].X])
				   k++, a1[b[j].X] = 1;
				if (!a2[b[j].Y])
				   k++, a2[b[j].Y] = 1;
			}
			if (k == x+y)
			   ans = max(ans,n-bits);
		}
		cout << ans << endl;
	}
	return 0;
}
