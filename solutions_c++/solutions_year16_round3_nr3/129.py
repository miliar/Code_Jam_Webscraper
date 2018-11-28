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
#define N 228228
#define mx 100
#define sqval 1000
#define eps 1e-9
typedef int ll;
typedef long double ld;
using namespace std;
ll n,m,k,x,y,i,xx,yy,q,j, w, l;
ll a[55][55], b[55][55], c[55][55];
struct lalka {
	ll x,y,z;
};
ll super_ans[3] = {22102794,62580637,134217727};
lalka t[1005];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		printf("Case #%d: ", ii+1);
		ll J, P, S, K;
		cin >> J >> P >> S >> K;
		ll sz = 0;
		for (i = 1; i <= J; i++)
			for (j = 1; j <= P; j++)
				for (k = 1; k <= S; k++)
				{
					t[sz].x = i, t[sz].y = j, t[sz].z = k;
					sz++;
				}
		ll ans = 0;
		ll max1 = -1;
		if (J+P+S < 9)
		{
		for (i = 0; i < (1<<sz); i++)
		{
			for (k = 1; k <= 3; k++)
				for (j = 1; j <= 3; j++)
					a[k][j] = b[k][j] = c[k][j] = 0;
			ll bits = 0, flag = 1;
			for (j = 0; j < sz; j++)
				if ((i&(1<<j))!=0)
				{
					a[t[j].x][t[j].y]++;
					b[t[j].x][t[j].z]++;
					c[t[j].y][t[j].z]++;
					if (a[t[j].x][t[j].y] > K || b[t[j].x][t[j].z] > K || c[t[j].y][t[j].z] > K)
					   flag = 0;
					bits++;
				}
			if (flag && bits > max1)
			{
				max1 = bits;
				ans = i;
			}
		}
		}
		 else ans = super_ans[min(K-1,2)];
		ll kk = 0;
		for (j = 0; j < sz; j++)
			if ((ans&(1<<j)) != 0)
			   kk++;
		cout << kk << endl;
		for (j = 0; j < sz; j++)
			if ((ans&(1<<j)) != 0)
			   cout << t[j].x << " " << t[j].y << " " << t[j].z << endl;
	}
	return 0;
}
