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
long long readLongLong() {long long N = -1; scanf("%lld", &N); return N;}
string readString() {char buffer[1 << 20]; scanf("%s", buffer); return buffer;}
template <class T> ostream& operator << (ostream& o, const vector <T>& v) {o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";} 
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p) {o << "("; o << p.first << "," << p.second << ")"; return o;} 

const bool DEBUG = true; 
const double epsilon = 1e-8; 
const int infinite  = 1000000000; 
const LL infiniteLongLong = 1000000000000000000LL; 

const int totalSize = 10000000 + 1;
const double eps = 1e-2;

struct Solver
{
	vector <int> total;
	bool isPalindrome(long long x) {
		long long rev = 0;
		long long fwd = x;
		while (x) {
			rev = rev * 10 + (x % 10);
			x /= 10;
		}
		return fwd == rev;
	}
	void preProcess() {
		total.resize(totalSize, 0);
		for (int i = 1; i < totalSize; ++i)
			if (isPalindrome(i) && isPalindrome(1LL * i * i))
				total[i] = total[i - 1] + 1;
			else
				total[i] = total[i - 1];
	}
	int solve(long long A, long long B) {
		int sqrtA = sqrt(1.0 * A + eps), sqrtB = sqrt(1.0 * B + eps);
		if (1LL * sqrtA * sqrtA == A) sqrtA--;
		return total[sqrtB] - total[sqrtA];
	}
};

int main()
{
	Solver solver;
	solver.preProcess();
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		long long A = readLongLong(), B = readLongLong();
		int result = solver.solve(A, B);
		printf("Case #%d: %d\n", test, result);
	}
	return 0;
}

// Powered by PhoenixAI
