// yousfi.saad+cp@gmail.com

#include <iostream>		// cin cout
#include <fstream>		// ifstream ofstream
#include <cmath>		// pow log2 log sqrt ceil floor exp exp2 cos sin 
#include <complex>		// complex<double> first (2.0,2.0);
#include <cstddef>		// size_t
#include <utility>		// make_pair swap
#include <functional>   // greater
#include <algorithm>	// sort ...
#include <string>          
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
using namespace std;

#define minmac(a,b) (a<b?a:b)
#define maxmac(a,b) (a>b?a:b)

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ull> vull;
typedef pair<int, int> ii;
typedef pair<ull, ull> ullull;
typedef vector<ii> vii;
typedef vector<ullull> vullull;
typedef set<int> si;
typedef map<string, int> msi;

// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvll(c, it) \
for (vll::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvull(c, it) \
for (vull::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define FOR(i, N) \
for (int i = 0; i < (N); ++i)
#define all(v) \
v.begin(),v.end()
//#define pb push_back

#define INF 2000000000 // 2 billion
// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers


ull gcd(ull a, ull b) {
	return b == 0 ? a : gcd(b, a % b);
}

// global vars
string _path("C:/Users/Samsung U/Downloads/");
string _inFile("A-large");
ifstream fin(_path + _inFile + ".in");
ofstream fout(_path + _inFile + ".out");

ull Ttests;
ull N;
string s;
map<char, ull> alpha;
string dig[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int indices[] = { 0, 2 , 6, 8,		4, 3, 7,	   1,   5,   9 };
char ids[] = { 'Z', 'W', 'X', 'G', 'U', 'T', 'S', 'O', 'F', 'I' };

void solvet(ull t) {
	alpha.clear();
	fin >> s;
	for (char c : s) {
		alpha[c] ++;
	}
	map<int, int> solm;
	int i = 0;
	for (int ind : indices) {
		string& sdig = dig[ind];
		char c = ids[i];
		solm[ind] = alpha[ c ];
		for (char inc : sdig) {
			alpha[inc] -= solm[ind];
		}
		i++;
	}
	string sol;
	for (auto soli : solm) {
		for (int i = 0; i < soli.second; ++i) {
			sol += (char)(soli.first + '0');
		}
	}
	fout << sol;
}

void solve() {
	fin >> Ttests;
	for (int t = 1; t <= Ttests; ++t) {
		fout << "Case #" << t << ": ";


		solvet(t);


		fout << endl;
	}
}

int main() {

	solve();

	return 0;
}

