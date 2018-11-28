#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <ctime>
#include <iomanip>
#include <iterator>
#include <set>
#include <string>
#include <stack>
#include <cmath>
#include <stdio.h>
#include <cstring>


#define ii <int , int >


#define mp make_pair
#define all(v) v.begin(),v.end()
#define loop (i, n) for (int i = 0; i < n; i++)
#define pb push_back
#define sz(v) (int )v.size()
#define X first
#define Y second

#define Pi (x) printf("%d ", (x))
#define Pii (x, y) printf("%d %d ", (x), (y))
#define Piii (x, y, z) printf("%d %d %d", (x), (y), (z))
#define Pl (x) printf("%I64d ", (x))
#define Pll (x, y) printf("%I64d I64d ", (x), (y))
#define Plll (x, y, z) printf("%I64d I64d I64d ", (x), (y), (z))
#define Ps (x) printf("%s", (x))
#define Pe () printf("\n")
#define Pe1 (i) for (int j = 0; j < i; j++) printf(" ")

#define Si (x) scanf("%d",&x)
#define Sii (x, y) scanf("%d %d", (&x), (&y))
#define Siii (x, y, z) scanf("%d %d %d", (&x), (&y), (&z))
#define Sl (x) scanf("%I64d", (&x))
#define Sll (x, y) scanf("%I64d %I64d", (&x), (&y))
#define Slll (x, y, z) scanf("%I64d %I64d %I64d", (&x), (&y), (&z))
#define Ss (x) scanf("%s", (&x))

using namespace std;

typedef long long ll;
typedef vector <int > vi;
typedef vector <vi > vvi;
typedef map<ll, ll> mll;
typedef pair ii pii;
typedef vector <pii > vii;
typedef map ii mii;
typedef set <int > si;
typedef multiset <int > msi;
typedef multimap <int, int > mmi;
typedef vector <ll > vl;
typedef pair <ll, ll > pll;
typedef vector <pll > vll;


const ll nInf = -1000000000;
const ll pInf = 1000000000;
const ll mod = 1000000007;
const int MAXN = 101;

void getdata();
void preproc();
int solve();
int n;
char s[MAXN];
int a[MAXN];
int j;
vi bin;
void tobin(int mask, int mx);
ll tosys(int sys);


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t = 1;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		getdata();
		preproc();
		printf("Case #%d:\n", i + 1);
		solve();
	}
	return 0;
}

void getdata()
{
	scanf("%d %d", &n, &j);
	for (int i = 0; i < n; i++)
	{
		if (s[i] == '+')
		{
			a[i] = 1;
		}
		else
		{
			a[i] = 0;
		}
	}

}

void preproc()
{

}

int solve()
{
	int mx = (1 << (n - 2));
	vl powers;
	int cnt = 0;
	for (int i = 0; i < 11; i++)
	{
		ll p = 1;
		for (int l = 0; l < n - 1; l++)
		{
			p *= i;
		}
		powers.pb(p);
	}

	for (int mask = 0; mask < mx; mask++)
	{
		mll divs;
		set<ll> dd;
		if (cnt == j)
		{
			break;
		}
		tobin(mask, n - 2);
		for (int k = 2; k <= 10; k++)
		{
			ll num = tosys(k);
			for (ll l = 2; l * l < min(num, ll(1e6)); l++)
			{
				if (num % l == 0)
				{
					divs[k] = l;
					break;
				}
			}
		}
		if (sz(divs) == 9)
		{
			for (int k = 0; k < sz(bin); k++)
			{
				printf("%d", bin[k]);
			}

			for (int k = 2; k <= 10; k++)
			{
				printf(" %I64d", divs[k]);
			}
			printf("\n");
			cnt++;
		}
	}
	return 0;
}

void tobin(int mask, int mx)
{
	bin.clear();
	bin.pb(1);
	int i = 0;
	//	while (mask > 0)
	for (int i = 0; i < mx; i++)
	{
		bin.pb(mask % 2);
		mask /= 2;
	}
	bin.pb(1);
	reverse(all(bin));
}

ll tosys(int sys)
{
	ll p = 1;
	ll ans = 0;
	for (int i = sz(bin) - 1; i >= 0; i--)
	{
		ans += p * bin[i];
		p *= sys;
	}
	return ans;
}