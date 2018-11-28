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
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//freopen("output.txt","w",stdout);
	//ofstream f1("output2.txt");
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		cin >> s;
		ll n = s.size();
		ll k = 1;
		for (i = 0; i < n-1; i++)
			if (s[i] != s[i+1])
			{
				k++;
			}
		if (s[n-1] == '+')
		   k--;
		printf("CASE #%d: %lld\n",ii+1,k);
	}
	return 0;
}
