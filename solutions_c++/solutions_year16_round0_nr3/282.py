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
#define MOD2 (33LL+(ll)1e+17)
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
ll i,j,n,m,x,y,z,k,x1,y1,was_created,free_left,qq,l;
ll a[20];
string s;
vector <ll> f, g;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		cin >> n >> k;
		printf("CASE #%d:\n", ii+1);
		for (i = 1; i <= k; i++)
		{
			f.clear();
			ll y = i;
			while (y)
			{
				f.push_back(y%2);
				y /= 2;
			}
			reverse(f.begin(), f.end());
			ll sz = f.size();
			g.clear();
			g.push_back(1);
			for (j = 0; j < n/2-sz-2; j++)
				g.push_back(0);
			for (j = 0; j < sz; j++)
				g.push_back(f[j]);
			g.push_back(1);
			for (j = 0; j < n; j++)
				cout << g[j%(n/2)];
			for (j = 2; j <= 10; j++)
			{
				ll sum = 0;
				for (l = 0; l < n/2; l++)
					sum = sum*j + g[l];
				cout << " " << sum;
			}
			cout << endl;
		}
	}
	return 0;
}
