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
ll a[100500], b[100500], c[100500];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		printf("Case #%d:", ii+1);
		cin >> n;
		for (i = 0; i < n; i++)
			cin >> a[i];
		while(1)
		{
			ll sum = 0;
			k = 0;
			ll max1 = -1;
			for (i = 0; i < n; i++)
			{
				sum += a[i];
				if (a[i])
				{
				   if (k == 0)
					  x = i;
				   if (k == 1)
					  y = i;
				   k++;
				}
				if (a[i] > max1)
				{
					max1 = a[i];
					w = i;
				}
			}
			if (sum == 0)
			   break;
			if (k == 2 && a[x] == a[y])
			{
				printf(" %c%c", char(x+'A'), char(y+'A'));
				a[x]--;
				a[y]--;
			} else
			{
			  printf(" %c", char(w+'A'));
			  a[w]--;
			}
		}
		cout << endl;
	}
	return 0;
}
