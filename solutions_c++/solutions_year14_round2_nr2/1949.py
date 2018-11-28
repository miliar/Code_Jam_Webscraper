#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <memory>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <complex>
#include <hash_map>
#include <hash_set>

#pragma comment (linker, "/STACK:1000000000")

using namespace std;

#define pb push_back
#define pob pop_back
#define rs resize
#define as assign
#define lwb lower_bound
#define upb upper_bound
#define mp make_pair

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <ll> vl;
typedef vector <vl> vvl;
typedef vector <bool> vb;
typedef vector <vb> vvb;
typedef vector <string> vs;
typedef vector <char> vc;
typedef vector <vc> vvc;
typedef vector <vvi> vvvi;
typedef vector <vvvi> vvvvi;
typedef vector <vvl> vvvl;
typedef vector <vvvl> vvvvl;
typedef vector <vvb> vvvb;
typedef double db;
typedef long double ldb;
typedef vector <db> vdb;
typedef vector <ldb> vldb;
typedef pair <int, int> ii;
typedef pair <int, char> ic;
typedef pair <ll, ll> lll;
typedef pair <int, ll> il;
typedef pair <ll, int> li;
typedef vector <ii> vii;
typedef vector <ic> vic;
typedef vector <vic> vvic;
typedef vector <vii> vvii;
typedef vector <lll> vll;
typedef vector <vll> vvll;
typedef set <int> si;
typedef set <ii> sii;
typedef set <pair <int, bool> > sib;
typedef vector <si> vsi;
typedef map <int, int> mii;
typedef map <string, char> msc;
typedef map <char, int> mci;
typedef queue <int> qi;
typedef deque <int> di;
typedef stack <int> sti;

const ll inf = (ll)1e9 + 7;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		int a, b, d;
		cin >> a >> b >> d;
		int ans = 0;
		for (int j = 0; j < a; ++j)
			for (int k = 0; k < b; ++k)
				if (int(j & k) < d)
					++ans;
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
//	system("pause");
	return 0;
}