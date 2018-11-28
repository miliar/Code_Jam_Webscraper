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
ll a[100500];
ll ans[50];
string s, t;
ll Abs(ll x)
{
	return x>0?x:-x;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		cin >> s >> t;
		n = s.size();

		m = 100500;
		printf("Case #%d: ",ii+1);
		if (n == 1)
		{
			for (i = 0; i <= 9; i++)
				for (j = 0; j <= 9; j++)
				{
					if (s[0] != '?' && i+'0' != s[0])
					   continue;
					if (t[0] != '?' && j+'0' != t[0])
					   continue;
					if (Abs(i-j) < m || Abs(i-j) == m && i < x || Abs(i-j) == m && x == i && j < y)
					{
						m = Abs(i-j);
						x = i;
						y = j;
					}
				}
			cout << x << " " << y;
		}
		if (n == 2)
		{
			for (i = 0; i <= 99; i++)
				for (j = 0; j <= 99; j++)
				{
					if (s[1] != '?' && i%10+'0' != s[1])
					   continue;
					if (t[1] != '?' && j%10+'0' != t[1])
					   continue;
					if (s[0] != '?' && i/10+'0' != s[0])
					   continue;
					if (t[0] != '?' && j/10+'0' != t[0])
					   continue;
					if (Abs(i-j) < m || Abs(i-j) == m && i < x || Abs(i-j) == m && x == i && j < y)
					{
						m = Abs(i-j);
						x = i;
						y = j;
					}
				}
			if (x/10 != 0)
			cout << x;
			else
			cout << "0" << x;
			cout << " ";
			if (y/10 != 0)
			cout << y;
			else
			cout << "0" << y;
		}
		if (n == 3)
		{
			for (i = 0; i <= 999; i++)
				for (j = 0; j <= 999; j++)
				{
					if (s[2] != '?' && i%10+'0' != s[2])
					   continue;
					if (t[2] != '?' && j%10+'0' != t[2])
					   continue;
					if (s[1] != '?' && (i/10)%10+'0' != s[1])
					   continue;
					if (t[1] != '?' && (j/10)%10+'0' != t[1])
					   continue;
					if (s[0] != '?' && (i/100)%10+'0' != s[0])
					   continue;
					if (t[0] != '?' && (j/100)%10+'0' != t[0])
					   continue;
					if (Abs(i-j) < m || Abs(i-j) == m && i < x || Abs(i-j) == m && x == i && j < y)
					{
						m = Abs(i-j);
						x = i;
						y = j;
					}
				}
			if (x/100 != 0)
			   cout << x;
			else
			if (x/10 != 0)
				cout << "0" << x;
			else
				cout << "00" << x;
			cout << " ";
			if (y/100 != 0)
			   cout << y;
			else
			if (y/10 != 0)
				cout << "0" << y;
			else
				cout << "00" << y;
		}
		cout << endl;
	}
	return 0;
}
