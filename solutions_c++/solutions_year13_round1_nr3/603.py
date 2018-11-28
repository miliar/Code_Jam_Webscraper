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

bool solveA(int a, int b, int c, vector <int>& v) {
	vector <int> x(8, 0);
	for (int mask = 0; mask < 8; ++mask) {
		x[mask] = 1;
		if (mask & 1) x[mask] *= a;
		if (mask & 2) x[mask] *= b;
		if (mask & 4) x[mask] *= c;
	}
	vector <bool> seen(128, false);
	for (int i = 0; i < size(x); ++i)
		seen[x[i]] = true;
	for (int i = 0; i < size(v); ++i)
		if (!seen[v[i]]) return false;
	return true;
}

string solve(int N, int M, int K, vector <int>& v) {
	for (int a = 2; a <= M; ++a)
		for (int b = 2; b <= M; ++b)
			for (int c = 2; c <= M; ++c)
				if (solveA(a, b, c, v))
				return "" + string(1, '0' + a) + "" + string(1, '0' + b) + "" + string(1, '0' + c);
}

int main()
{
	int nTest = readInt();
	printf("Case #1:\n");
	for (int test = 1; test <= nTest; ++test) {
		int R = readInt(), N = readInt(), M = readInt(), K = readInt();
		for (int t = 0; t < R; ++t) {
			vector <int> v; for (int i = 0; i < K; ++i) v.push_back(readInt());
			printf("%s\n", solve(N, M, K, v).c_str());
		}
	}
	return 0;
}

// Powered by PhoenixAI
