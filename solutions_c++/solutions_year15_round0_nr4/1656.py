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

int solve();//1 - GABRIEL, 0 - RICHARD;

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0;i < t; i++)
	{
		int res = solve();
		printf("Case #%d: ", i + 1);
		if (res == 0)
			printf("RICHARD\n");
		else
			printf("GABRIEL\n");
	}
	return 0;
}

int solve()
{
	int x, c, r;
	scanf("%d %d %d", &x, &r, &c);
	int amountcels = r * c;
	if (x == 1)
		return 1;
	if (x == 2)
	{
		if (amountcels % 2 == 0)
			return 1;
		else 
			return 0;
	}
	if ( x == 3)
	{
		if (r == 1 || c == 1)
			return 0;
		if (amountcels % 3 == 0)
			return 1;
		else
			return 0;
	}
	if (x == 4)
	{
		if (r < 3 || c < 3)
			return 0;
		if (amountcels % 4 == 0)
			return 1;
		else
			return 0;
	}
}