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
typedef long long ll;
typedef long double ld;
using namespace std;
ll n,m,k,x,y,i,xx,yy,q,j, w, l;
ll a[55][55], b[100500], c[100500];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		printf("Case #%d: ", ii+1);
		cin >> n >> m;
		if (m > (1LL<<(n-2)))
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		for (i = 0; i < n; i++)
			for (j = i+1; j < n; j++)
				a[i][j] = 1;
		m = (1LL<<(n-2))-m;
		for (i = 1; i < n-1; i++)
			if (m >= (1LL<<(n-i-2)))
			{
				m -= (1LL<<(n-i-2));
				a[0][i] = 0;
			}
		cout << "POSSIBLE" << endl;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
				cout << a[i][j];
			cout << endl;
		}
	}
	return 0;
}
