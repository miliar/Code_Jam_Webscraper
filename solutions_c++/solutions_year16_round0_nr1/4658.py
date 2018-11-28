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
const int MAXN = 1000;

void getdata();
void preproc();
int solve();
int n;
void convert(int num);

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
		int ans = solve();
		if (ans != -1)
		{
			printf("Case #%d: %d\n", i+1, ans);
		}
		else
		{
			printf("Case #%d: INSOMNIA\n", i+1);
		}
	}
	return 0;
}

void getdata()
{
	scanf("%d", &n);

}

void preproc()
{

}
vi cur;

int solve()
{
	vi digits(10, 0);
	int cnt = 0;
	for (int i = 1; i < 1000; i++)
	{
		convert(n * i);
		for (int j = 0; j < sz(cur); j++)
		{
			if (digits[cur[j]] == 0)
			{
				cnt++;
				digits[cur[j]] = 1;
			}
		}
		if (cnt == 10)
		{
			return n * i;
		}
	}
	return -1;
}


void convert(int num)
{
	cur.clear();
	while (num > 0)
	{
		cur.pb(num % 10);
		num /= 10;
	}
}