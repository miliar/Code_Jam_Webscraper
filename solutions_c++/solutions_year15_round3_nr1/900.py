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

#define ii <int , int>


#define mp make_pair
#define all(v) v.begin(),v.end()
#define loop(i, n) for (int i = 0; i < n; i++)
#define pb push_back
#define sz(v) (int)v.size()
#define X first
#define Y second


using namespace std;

typedef long long ll;
typedef vector<int > vi;
typedef vector<vi> vvi;
typedef pair ii pii;
typedef vector <pii> vii;
typedef map ii mii;
typedef set <int > si;
typedef multiset <int > msi;
typedef multimap <int , int> mmi;


const ll nInf = -1000000000;
const ll pInf = 1000000000;
const ll mod  = 1000000007;

void solve();
int solve1(int r, int c, int w);
void solve2();

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
//		solve();
		solve2();
	}
	return 0;
}

void solve()
{
	int r, c, w;
	scanf("%d %d %d", &r, &c, &w);
	if (c == w)
	{
		printf("%d\n", w);
		return;
	}
	if (w == 1)
	{
		printf("%d\n", c);
		return;
	}
	if (w == (c - 1) / 2)
	{
		printf("%d\n", w + 2);
		return;
	}
	if (w >= c / 2)
	{
		printf("%d\n", w + 1);
		return;
	}
	if (w == 2 && c == 6)
	{
		printf("%d\n", 4);
		return;
	}
	if (w == 2 && c == 7)
	{
		printf("%d\n", 5);
		return;
	}
	if (w == 2 && c == 8)
	{
		printf("%d\n", 5);
		return;
	}
	if (w == 2 && c == 9)
	{
		printf("%d\n", 6);
		return;
	}
	if (w == 2 && c == 10)
	{
		printf("%d\n", 6);
		return;
	}
	if (w == 3 && c == 10)
	{
		printf("%d\n", 6);
		return;
	}
	if (w == 3 && c == 9)
	{
		printf("%d\n", 5);
		return;
	}
	if (w == 3 && c == 8)
	{
		printf("%d\n", 5);
		return;
	}

	if (w == 4 && c == 10)
	{
		printf("%d\n", 6);
		return;
	}
}


void solve2()
{
	int r, c, w;
	scanf("%d %d %d", &r, &c, &w);
	int res = solve1(1, c, w);
	res = res + (r - 1) * (c / w);
	printf("%d\n", res);
}
int solve1(int r, int c, int w)
{
	if (w == c)
		return w;
	if (w == 1)
		return c;
	if (w >= (c + 1) / 2)
	{
		return w + 1;
	}
	else
	{
		return solve1(r, c - w, w) + 1;
	}
}