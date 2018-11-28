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
ll n,m,i,j,k,l,r,x,y,z,ans;
ll a[100050], b[100500], used[100500];
ll dp[13][5000];
string s = "RSP", t;
vector <string> f;
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
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		printf("Case #%d: ", ii+1);
		ll n,P,R,S;
		cin >> n >> R >> P >> S;
		f.clear();
		for (i = 0; i < 3; i++)
		{
			ll P1 = 0, R1 = 0, S1 = 0;
   			dp[0][0] = i;
			for (j = 0; j < n; j++)
			{
				for (k = 0; k < (1<<j); k++)
				{
					dp[j+1][k*2] = dp[j][k];
					dp[j+1][k*2+1] = (dp[j][k]+1)%3;
					if (s[dp[j+1][k*2]] > s[dp[j+1][k*2+1]])
					   swap(dp[j+1][k*2], dp[j+1][k*2+1]);
				}
			}
			for (j = 0; j < (1<<n); j++)
				if (dp[n][j] == 0)
				   R1++;
				else
				if (dp[n][j] == 1)
				   S1++;
				else
					P1++;
			if (P1 == P && R1 == R && S1 == S)
			{
				t.clear();
				for (j = 0; j < (1<<n); j++)
					t.push_back(s[dp[n][j]]);
				t = norm(t, n);
				f.push_back(t);
			}
		}
		sort(f.begin(), f.end());
		if (f.size() == 0)
		   cout << "IMPOSSIBLE" << endl;
		else
			cout << f[f.size()-1] << endl;
	}
	return 0;
}
