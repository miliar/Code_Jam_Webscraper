/*********** Includes *************************************************/
#ifdef DEBUG
#ifndef _GLIBCXX_DEBUG
#define _GLIBCXX_DEBUG
#endif
#endif

// Streams
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>

// STL containers
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <list>

// Other STL
#include <iterator>
#include <functional>
#include <numeric>
#include <algorithm>

// C heritage
#include <cstdio>
#include <cassert>
#include <cstdint>

/************* Debug macros and exceptions ****************************/
#ifdef DEBUG
	#define dbg_assert(x) assert(x);
	#define dbg(x) std::cerr << "DBG<" << __LINE__ << "> " << #x << " = " << x << std::endl;
#else
	#define dbg_assert(x)
	#define dbg(x)
#endif

typedef		int32_t						int32;
typedef		int64_t						int64;
typedef		uint32_t					uint32;
typedef		uint64_t					uint64;

// Standard types
typedef 		std::pair<int32,int32>		ii;
typedef 		std::vector<int32>			vi;
typedef			std::vector<ii> 			vii;
typedef			std::vector<vi>				vvi;
typedef			std::set<int32>				si;
typedef			std::map<int32,int32>		mii;
typedef			std::map<int32,vi>			mivi;
typedef			std::stringstream			ss;

// Standard aliases
#define			pb							push_back

/************* Pretty print containers ********************************/

// Vectors
template<typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T>& v)
{
	os << "[";
	for (
         auto i = v.begin();
         i != v.end() && os << *i;
         (++i != v.end()) ? os << ", " : os
         );
	return os << "]";
}

// Sets
template<typename T>
std::ostream& operator<<(std::ostream& os, const std::set<T>& v)
{
	os << "{";
	for (auto i = v.begin(); i != v.end() && os << *i; (++i != v.end()) ? os << ", " : os)
		;
	return os << "}";
}

// Pairs
template<typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& v)
{
	return os << "(" << v.first << ", " << v.second << ")";
}

// Maps
template<typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::map<T1, T2>& v)
{
	os << "{";
	for (
         auto i = v.begin();
         i != v.end() && os << "[" << i->first << "]: " << i->second;
         (++i != v.end()) ? os << ", " : os
         );
	
	return os << "}";
}

// Unordered maps
template<typename T1, typename T2>
std::ostream& operator<<(std::ostream& os, const std::unordered_map<T1, T2>& v)
{
	os << "{";
	for (
         auto i = v.begin();
         i != v.end() && os << "[" << i->first << "]: " << i->second;
         (++i != v.end()) ? os << ", " : os
         );
	
	return os << "}";
}

// Bitset
template<size_t N>
std::ostream& operator<<(std::ostream& os, const std::bitset<N>& v)
{
	return os << v.to_string();
}
/**********************************************************************/


////////////////////////////////////////////////////////////////////////
// Actual solution goes down here                                     //
////////////////////////////////////////////////////////////////////////

using namespace std;

int get(vi& S, int idx) {
	if (idx >= (int)S.size()) return 0;
	else return S[idx];
}

bool feas(vi& S, int cur, int X) {
	if (2*cur < (int)S.size()) return false;

	for (int i=0; i<cur; i++) {
		int a = get(S,i), b = get(S,2*cur-i-1);

		if (a+b > X) return false;
	}

	return true;
}

void testcase(int testno) {
	int N, X;
	cin >> N >> X;
	
	vi S(N);
	for (int i=0; i<N; i++)
		cin >> S[i];

	sort(S.begin(), S.end(), greater<int>());
	//cout << S << endl;

	int lb = 1, ub = 10005;

	int ans = ub;
	while (lb <= ub) {
		int cur = (lb + ub) / 2;
		if (feas(S, cur, X)) {
			ans = cur;
			ub = cur-1;
		} else {
			lb = cur+1;
		}
	}

	cout << "Case #" << testno << ": " << ans << endl;

}

int main() {

	int T;

	cin >> T;
	for (int i=0; i<T; i++) testcase(i+1);

    return 0;
}