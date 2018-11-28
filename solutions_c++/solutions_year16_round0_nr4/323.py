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
	//freopen("input.txt","r",stdin);
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		ll K, C, S;
		cin >> K >> C >> S;
		ll sz = (K-1)/C+1;
		if (sz > S)
		{
			printf("CASE #%d: IMPOSSIBLE\n",ii+1);
			continue;
		}
		printf("CASE #%d:",ii+1);
		for (i = 0; i < sz; i++)
		{
			ll ans = 0;
			for (j = i*C; j < i*C + C; j++)
				ans = ans*K + j%K;
			ans++;
			cout << " " << ans;
		}
		cout << endl;
	}
	return 0;
}
