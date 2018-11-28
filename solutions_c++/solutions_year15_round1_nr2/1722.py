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

#define ii <int , int>


#define mp make_pair
#define all(v) v.begin(),v.end()
#define loop(i, n) for (int i = 0; i < n; i++)
#define pb push_back
#define sz(v) v.size()


using namespace std;

typedef long long ll;
//typedef int ll;
typedef vector<int > vi;
typedef vector<vi> vii;
typedef pair ii pii;
typedef map ii mii;
typedef set <int > si;
typedef multiset <int > msi;
typedef multimap <int , int> mmi;

// const int nInf = -1000000000;
// const int pInf = 1000000000;
// const int mod  = 1000000007;
const ll nInf = -1000000000;
const ll pInf = 1000000000;
const ll mod  = 1000000007;
ll solve();
ll gcd(int *m, int b);
vi divisors(int a);

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t; i++)
	{
		ll res = solve();
		printf("Case #%d: %I64d\n", i + 1, res);
	}
	return 0;
}

ll solve()
{
	int b, n;
	scanf("%d %d", &b, &n);
	int *m = new int[b];
	ll *timefree = new ll[b];
	for (int i = 0;i < b; i++)
	{
		scanf("%d", &m[i]);
	}

	fill(timefree, timefree + b, 0);
	ll g = gcd(m, b);
	int count1 = 0;
	for (int i = 0; i < b; i++)
	{
		count1 += g / m[i];
	}
// 	if (n == 915742169)
// 	{
// 		int y = 0;
// 	}
	n = (n) % (count1);
	if (n == 0)
	{
		int indexmin = -1;
		int min1 = pInf;
		for (int i = 0;i < b; i++)
		{
			if (min1 >= m[i])
			{
				min1 = m[i];
				indexmin = i;
			}
		}
		return indexmin + 1;
	}
	ll num = 1;
	ll time = 0;
	for (int i = 0;i < n;)
	{
		for (int j = 0; j < b; j++)
		{
			if (timefree[j] == time)
			{
				timefree[j] += m[j];
				i++;
				if (i % 137 == 0)
				{
					int kjh = 0;
				}
				if (i == n)
				{
					return j + 1;
				}
			}
		}
		ll mintime = pInf * pInf;
		for (int j = 0; j< b; j++)
		{
			if (mintime > timefree[j])
				mintime = timefree[j];
		}
		time = mintime;
	}
	for (int j = 0; j < b; j++)
	{
		if (timefree[j] == time)
		{
			timefree[j] += m[j];
			return j + 1;
		}
	}
//	return 
}

ll gcd(int *m, int b)
{
	vi *divs = new vi[b];

	for (int i = 0;i < b; i++)
	{
		divs[i] = divisors(m[i]);
	}
	int *maxpow = new int[25];
	for (int i = 2; i <25; i++)
	{
		int count = 0;
		int maxcount = 0;
		for (int k = 0; k < b; k++)
		{
			count = 0;
			for (int j = 0; j < divs[k].size(); j++)
			{
				if (divs[k][j] == i)
					count++;
			}
			if (count > maxcount)
				maxcount = count;
		}
		maxpow[i] = maxcount;
	}
	ll g = 1;
	for (int i = 2; i < 25; i++)
	{
		for (int j = 0; j < maxpow[i]; j++)
			g *= i;
	}
	return g;
}

vi divisors(int a)
{
	vi res ;
	for (int i = 2; i <= a; i++)
	{
		if (a % i == 0)
		{
			a = a / i;
			res.push_back(i);
			i = 1;
		}
	}
	return res;
}