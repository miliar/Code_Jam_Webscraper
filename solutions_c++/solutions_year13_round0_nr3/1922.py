#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }

template<class T>
string i2s(const T &a)
{
	oss os; os << a;
	return os.str();
}

bool is_palin(LL x)
{
	string s = i2s(x);
	for(int i = 0; i < s.size() / 2; ++i)
		if(s[i] != s[s.size() - i - 1])
			return false;
	return true;
}

vector<LL> good;

void precalc()
{
	int sq = 10000001;
	for(int i = 1; i <= sq; ++i)
	{
		if(is_palin(i))
		{
			if(is_palin(LL(i) * i))
				good.pb(LL(i) * i);
		}
	}
}

void solve(int test)
{
	LL a, b;
	cin >> a >> b;


	int res = upper_bound(good.begin(), good.end(), b) - lower_bound(good.begin(), good.end(), a);

	cout << T(test) << " " << res << endl;
}

int main()
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	clock_t tstart = clock();
	precalc();
	dbg((clock() - tstart) / LD(CLOCKS_PER_SEC));
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test)
		solve(test);
	dbg((clock() - tstart) / LD(CLOCKS_PER_SEC));
	return 0;
}
/*************************
*************************/
#endif
