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
string readString() {char buffer[1 << 20]; scanf("%s", buffer); return buffer;}
template <class T> ostream& operator << (ostream& o, const vector <T>& v) {o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";} 
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p) {o << "("; o << p.first << "," << p.second << ")"; return o;} 

const bool DEBUG = true; 
const double epsilon = 1e-8; 
const int infinite  = 1000000000; 
const LL infiniteLongLong = 1000000000000000000LL; 

map <long long, map <int, int> > memo;
map <long long, map <int, bool> > seen;

struct Solver
{
	int rsolve(int start, int idx, vector <int>& v) {
		if (idx == v.size()) return 0;
		else {
			if (seen[start][idx])
				return memo[start][idx];
			seen[start][idx] = true;
			int& result = memo[start][idx] = infinite;
			if (v[idx] < start)
				return result = rsolve(start + v[idx], idx + 1, v);
			if (start != 1)
				result = min(result, 1 + rsolve(2 * start - 1, idx, v));
			result = min(result, 1 + rsolve(start, idx + 1, v));
			return result;
		}
	}
	int solve(int start, vector <int>& v) {
		memo.clear();
		seen.clear();
		sort(v.begin(), v.end());
		return rsolve(start, 0, v);
	}
};

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		int A = readInt(), N = readInt();
		vector <int> v(N, 0);
		for (int i = 0; i < N; ++i)
			v[i] = readInt();
		Solver solver;
		int answer = solver.solve(A, v);
		printf("Case #%d: %d\n", test, answer);
	}
	return 0;
}

// Powered by PhoenixAI
