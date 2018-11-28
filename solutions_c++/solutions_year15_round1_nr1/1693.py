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
typedef vector<int > vi;
typedef vector<vi> vii;
typedef pair ii pii;
typedef map ii mii;
typedef set <int > si;
typedef multiset <int > msi;
typedef multimap <int , int> mmi;

const ll nInf = -1000000000;
const ll pInf = 1000000000;
const ll mod  = 1000000007;

pii solve();

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t; i++)
	{
		pii res = solve();
		printf("Case #%d: %d %d\n", i + 1, res.first, res.second);
	}
	return 0;
}

pii solve()
{
	int n;
	scanf("%d", &n);
	int *m = new int[n];
	for (int i = 0;i < n; i++)
	{
		scanf("%d", &m[i]);
	}
	int firstmin = 0;
	for (int i = 1; i < n; i++)
	{
		if (m[i] < m[i - 1])
			firstmin += m[i - 1] - m[i];
	}
	int secondmin = 0;
	int maxdiffer = 0;
	for (int i = 0;i < n - 1; i++)
	{
		if (m[i] - m[i + 1] > maxdiffer)
			maxdiffer = m[i] - m[i + 1];
	}
	double speed = 0;
//	if (maxdiffer % 10 == 0)
	{
		speed = maxdiffer / 10.0;
	}
//	else
//		speed = maxdiffer / 10.0 + 1;
	for (int i = 0;i < n - 1; i++)
	{
		if (speed * 10 > m[i])
			secondmin += m[i];
		else
			secondmin += speed * 10;
	}
	return mp(firstmin, secondmin);
}
