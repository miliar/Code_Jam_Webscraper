#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define repeat(t) for (int asdfg=0; asdfg < (t); asdfg++)
#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define odd(x) (bool((x)&1))
#define even(x) (bool((x)&1^1))
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef vector<pii> vpii;

int a,b;
inline bool check(ll x)
{
	vi a;
	while (x)
	{
		a.pb(x%10);
		x/=10;
	}
	int n=a.size();
	for (int i=0; i<n/2; i++) if (a[i]!=a[n-i-1]) return false;
	return true;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);

	int cas;
	scanf("%d",&cas);
	for (int t=1; t<=cas; t++)
	{
		scanf("%d%d",&a,&b);
	    ll l=(int)sqrt(a); if (l*l<a) l++;
		ll r=(int)sqrt(b);
		int cnt=0;
		for (ll x=l; x<=r; x++) if (check(x) && check(x*x))
			cnt++;
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}