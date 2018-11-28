#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;


#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "problem"


bool check(LL b)
{	
	vector <int> a1,b1;
	LL a = b * b;
	while(b)
	{
		b1.pb(b % 10);
		b /= 10;
	}
	int n = b1.size();
	for (int i = 0; i < n; i++)
	{
	   if (b1[i] != b1[n - 1 - i])
		   return false;
	}
	while(a)
	{
		a1.pb(a % 10);
		a /= 10;
	}
	n = a1.size();
	for (int i = 0; i < n; i++)
	{
	   if (a1[i] != a1[n - 1 - i])
		   return false;
	}
	return true;
}
LL tmp[39] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
	START
	freopen("C-small-attempt0.in","r",stdin);freopen("output2.txt","w",stdout);
	/*vector <LL> good;
	for (LL i = 1; i <= 10000000; i++)
	{
		if (check(i))
		{
			good.pb(i * i);
		}
	}
	cout << good.size() << endl;
	cout << "{";
	for (int i = 0; i < good.size(); i++)
	{
		cout << good[i] << ",";
	}
	cout << "}" << endl; */
	
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++)
	{
		LL l, r;
		scanf("%I64d %I64d", &l, &r);
		int p1 = upper_bound(tmp, tmp + 38, r) - tmp - 1;
		int p2 = lower_bound(tmp, tmp + 38, l) - tmp;
		printf("Case #%d: %d\n", test, max(0, p1 - p2 + 1));
	}
	
	END
    return 0;
}
/*******************************************
*******************************************/
#endif