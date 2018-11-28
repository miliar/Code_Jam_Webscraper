#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>

using namespace std; 

#define BUG(x) if (DEBUG) cout << __LINE__ << ": " << #x << " = " << x << endl; 
#define LET(x, a) __typeof(a) x = a
#define FOREACH(it, v) for(LET(it, (v).begin()); it != (v).end(); ++it) 

typedef long long LL; 

template <class T> inline int size(const T& c) {return (int) c.size();} 
inline LL two(int x) {return (1LL << (x));}
int readInt() {int N = -1; scanf("%d", &N); return N;}
string readString() {char buffer[1 << 22]; scanf("%s", buffer); return buffer;}
template <class T> ostream& operator << (ostream& o, const vector <T>& v) {o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";} 
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p) {o << "("; o << p.first << "," << p.second << ")"; return o;} 

const bool DEBUG = true; 
const double epsilon = 1e-8; 
const int infinite  = 1000000000; 
const LL infiniteLongLong = 1000000000000000000LL; 

struct Solver
{
	vector < long long > dp;
	long long solve(string& s, int N) {
		dp.clear();
		dp.resize(size(s), 0);
		vector <bool> alpha(256, 0);
		alpha['a'] = alpha['e'] = alpha['i'] = alpha['o'] = alpha['u'] = true;
		for (int i = size(s) - 1; i >= 0; --i)
			dp[i] = alpha[s[i]]? 0 : 1;
		vector <int> nextTrue(size(s), 0);
		int nTrue = -1;
		for (int i = size(s) - 2; i >= 0; --i) {
			if (dp[i] != 0)
				dp[i] += dp[i + 1];
		}
		for (int i = size(s) - 1; i >= 0; --i) {
			if (dp[i] >= N) {
				nTrue = i;
			}
			nextTrue[i] = nTrue;
		}
		long long result = 0;
		for (int i = 0; i < size(s); ++i) {
			int r = nextTrue[i];
			if (r != -1) {
				result += (size(s) - 1) - (r + N - 1) + 1;
			}
		}
		return result;
	}
};

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		string s = readString();
		int N = readInt();
		Solver solver;
		long long result = solver.solve(s, N);
		printf("Case #%d: %lld\n", test, result);
	}
	return 0;
}

// Powered by PhoenixAI
