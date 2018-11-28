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

int bestResult = -1;

int recurse(int gain, int currEnergy, int maxEnergy, int regain, int N, vector <int>& v, int idx) {
	if (idx == N) {
		if (gain > bestResult) {
			bestResult = gain;
		}
	}
	else {
		for (int e = currEnergy; e >= 0; --e) {
			recurse(gain + e * v[idx], min(currEnergy - e + regain, maxEnergy), maxEnergy, regain, N, v, idx + 1);
		}
	}
}

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		int E = readInt(), R = readInt(), N = readInt();
		vector <int> v;
		for (int i = 0; i < N; ++i)
			v.push_back(readInt());
		bestResult = -1;
		recurse(0, E, E, R, N, v, 0);
		printf("Case #%d: %d\n", test, bestResult);
	}
	return 0;
}

// Powered by PhoenixAI
