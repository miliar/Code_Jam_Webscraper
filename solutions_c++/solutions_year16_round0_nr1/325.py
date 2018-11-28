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
void bla(ll x)
{
	while (x)
	{
		a[x%10] = 1;
		x /= 10;
	}
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//freopen("output.txt","w",stdout);
	//ofstream f1("output2.txt");
	ll tests;
	cin >> tests;
	for (int ii = 0; ii < tests; ii++)
	{
		cin >> n;
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", ii+1);
			continue;
		}
		for (i = 0; i < 10; i++)
			a[i] = 0;
		for (i = 1; i <= 1000; i++)
		{
			bla(i*n);
			ll sum = 0;
			for (j = 0; j < 10; j++)
				sum += a[j];
			if (sum == 10)
			{
				printf("Case #%d: %lld\n", ii+1, i*n);
				break;
			}
		}
	}
	return 0;
}
