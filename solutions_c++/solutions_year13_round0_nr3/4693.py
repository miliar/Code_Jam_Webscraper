//Solution by Miras Myrzakerey
//Look at my code
//My code is amazing

#include <cstdio>
#include <iostream>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <ctime>
#include <queue>
#include <iomanip>

using namespace std;

#define INF 1000000001
#define sqr(x) (x) * (x)
#define maxn 200001
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define all(a) a.begin(),a.end()
#define len(a) (int)(a.length())
#define F first
#define S second
#define pii pair<int,int>
#define LL long long
#define vi vector<int>
#define forn(xx,yy,zz) for(int zz = xx; zz <= yy; ++zz)
#define forl(xx,yy,zz) for(int zz = xx; zz >= yy; --zz)
#define str string
#define eps 1e-7
#define pi M_PI
#define fill(x,y) memset((x), (y), sizeof((x)))
#define sz(x) (int)(x).size()
#define read(x) scanf("%d",&x)

int t;
LL a[100] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201ll, 104060401ll, 121242121ll, 123454321ll, 125686521ll, 400080004ll, 404090404ll, 10000200001ll, 10221412201ll, 12102420121ll, 12345654321ll, 40000800004ll, 1000002000001ll, 1002003002001ll, 1004006004001ll, 1020304030201ll, 1022325232201ll, 1024348434201ll, 1210024200121ll, 1212225222121ll, 1214428244121ll, 1232346432321ll, 1234567654321ll, 4000008000004ll, 4004009004004ll};
LL l, r;

LL f (LL r)
{
	int ans = 38;

	while (a[ans] > r)
		ans--;

	return ans;		
}

int main()
{
	freopen ("in", "r", stdin);
	freopen ("out", "w", stdout);

	scanf ("%d", &t);

	for (int it = 1; it <= t; ++it)
	{
		scanf ("%I64d%I64d", &l, &r);

		printf ("Case #%d: %I64d\n", it, f (r) - f (l - 1));
	}
}