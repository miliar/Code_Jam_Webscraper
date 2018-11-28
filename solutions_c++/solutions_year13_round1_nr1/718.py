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
long long readLL() {long long N = -1; scanf("%lld", &N); return N;}
string readString() {char buffer[1 << 20]; scanf("%s", buffer); return buffer;}
template <class T> ostream& operator << (ostream& o, const vector <T>& v) {o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";} 
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p) {o << "("; o << p.first << "," << p.second << ")"; return o;} 

const bool DEBUG = true; 
const double epsilon = 1e-8; 
const int infinite  = 1000000000; 
const LL infiniteLongLong = 1000000000000000000LL; 

double f(double mid, double r)
{
	return (2.0 * r - 3) * mid + 2.0 * (mid) * (mid + 1);
}
double find(long long low, long long high, double r, double t) {
	long long mid = ((double) low + high + 1) / 2;
	if (f(mid, r) <= t && f(mid + 1, r) > t)
		return mid;
	else if (f(mid, r) <= t)
		return find(mid + 1, high, r, t);
	else
		return find(low, mid - 1, r, t);
}

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		double r = readLL(), t = readLL();
		long long low = 1, high = (1LL << 62);
		long long result = find(low, high, r, t);
		printf("Case #%d: %lld\n", test, result);
	}
	return 0;
}

// Powered by PhoenixAI
