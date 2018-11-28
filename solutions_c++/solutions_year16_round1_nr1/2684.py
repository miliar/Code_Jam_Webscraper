#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

#define	loo(i,a,b)	for(auto i=a;i<b;i++)
#define	rep(i,b)	loo(i,0,b)
#define dow(i,b)	for(auto i=b-1;i>=0;i--)

#define sz(a)		((int)(a.size()))
#define all(a)		a.begin(),a.end()
#define in(a,e)		((a).find(e)!=(a).end())

typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ui> vui;
typedef vector<ll> vll;
typedef vector<ull> vull;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef unordered_set<int> unsi;
typedef unordered_map<int, int> unmii;
typedef long double ld;

const int mv4[4][2] = { { 0,1 },{ 0,-1 },{ 1,0 },{ -1,0 } };
const int mv8[8][2] = { { 0,1 },{ 0,-1 },{ 1,0 },{ -1,0 },{ 1,1 },{ 1,-1 },{ -1,1 },{ -1,-1 } };
const int inf = (int)1e9;
const char *boo[2] = { "NO","YES" };
const char *inv = "Impossible";
inline void term(const string &msg = inv) { cout << msg << endl; exit(0); }

const char *fin = "in.txt";
const char *fout = "out.txt";

//#define SUBMIT	//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

int main() {
#ifndef SUBMIT
	freopen(fin, "r", stdin);
	freopen(fout, "w", stdout);
#endif
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);

	int T;
	cin >> T;
	rep(K, T) {
		cerr << K << '\n';

		string s;
		cin >> s;

		string r;

		for (auto c : s)
			if (r.size() && c < r[0])
				r.push_back(c);
			else
				r.insert(r.begin(), c);
		cout << "Case #" << K + 1 << ": " << r << '\n';
	}
	exit(0);
}
