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
bool check(vi cur, int v);
vi getbits(int x);

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}

void solve()
{
	int d, c, v;
	scanf("%d %d %d", &c, &d, &v);
	vi cur(d);
	for (int i = 0;i < d; i++)
	{
		scanf("%d", &cur[i]);
	}
	bool *isp = new bool[v];
	fill(isp, isp + v,  false);

	for (int i = 1;i < (1<<d); i++)
	{
		vi bits =getbits(i);
		int sum = 0;
		for (int j = 0;j < sz(bits); j++)
		{
			if (bits[j] == 1)
				sum+= cur[j];
		}
		if (sum <= v)
			isp[sum - 1] = true;
	}
	bool b = false;
	int count = 0;
	for (int i = 0;i < v; i++)
	{
		if (isp[i] == false)
		{
			b = true;
			count++;
		}
	}
	if (!b)
	{
		printf("%d\n", 0);
		return;
	}

	if (count == 1)
	{
		printf("%d\n", 1);
		return;

	}


	int res = 0;
	for (int i = 0; i < v; i++)
	{
		if (!isp[i])
		{
			cur.pb(i + 1);
			sort(cur.begin(), cur.end());
			res++;
			bool ch = check(cur, v);
			if (ch)
			{
				printf("%d\n", res);
				return;
			}
			fill(isp, isp + v,  false);
			d = sz(cur);
			for (int i = 1;i < (1<<d); i++)
			{
				vi bits =getbits(i);
				int sum = 0;
				for (int j = 0;j < sz(bits); j++)
				{
					if (bits[j] == 1)
						sum+= cur[j];
				}
				if (sum <= v)
					isp[sum - 1] = true;
			}


		}
	}


}


vi getbits(int x)
{
	vi res;
	while (x != 0)
	{
		res.pb(x % 2);
		x = x / 2;
	}
//	reverse(res.begin(), res.end());
	return res;
}

bool check(vi cur, int v)
{
	int d = sz(cur);
	bool *isp = new bool[v];
	fill(isp, isp + v,  false);

	for (int i = 1;i < (1<<d); i++)
	{
		vi bits =getbits(i);
		int sum = 0;
		for (int j = 0;j < sz(bits); j++)
		{
			if (bits[j] == 1)
				sum+= cur[j];
		}
		if (sum <= v)
			isp[sum - 1] = true;
	}
	bool b = false;
	int count = 0;
	for (int i = 0;i < v; i++)
	{
		if (isp[i] == false)
		{
			b = true;
			count++;
		}
	}
	if (!b)
		return true;
	else
		return false;
}