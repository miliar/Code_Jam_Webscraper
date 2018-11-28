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

int solve();

int main()
{
	freopen( "input.txt", "r" , stdin);
	freopen( "output.txt", "w" , stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		int res = solve();
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}

int solve()
{
	int s;
	scanf("%d", &s);

	char *shy = new char[s + 10] ;
	scanf("%s", shy);
	int sum = 0;
	int friends = 0;
	int b = 0;
	for (int i = 0;i <= s; i++)
	{
		if (sum < i && shy[i] != '0')
		{
			b = i - sum;
			friends += (i - sum);
			sum += b;
		}
		sum += shy[i] - '0';
	}
	return friends;
//	printf("")
}