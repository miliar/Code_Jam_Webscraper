/*********** Includes *************************************************/
#ifdef DEBUG
// #ifndef _GLIBCXX_DEBUG
// #define _GLIBCXX_DEBUG
// #endif
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

struct node {
	map<char, node*> next;
};

struct trie {

	node* root;
	int sz;

	trie() {
		sz = 1;
		root = new node();
	}

	void add(string s) {
		node *n = root;
		for (char ch: s) {
			if (!(n->next).count(ch)) {
				++sz;
				(n->next)[ch] = new node;
			}
			n = (n->next)[ch];
		}
	}
};

int calc(vector<string>& sts) {
	trie T;
	for (string s: sts)
		T.add(s);
	return T.sz;
}

void testcase(int testno) {

	int M, N;
	cin >> M >> N;
	vector<string> strs(M);
	for (int i=0; i<M; i++) cin >> strs[i];
	mii res;

	vi srv(M);
	while (true) {
		bool good = true;
		for (int srvr = 0; srvr < N; srvr++) {
			int count = 0;
			for (int i=0; i<M; i++)
				count += (srv[i] == srvr);
			if (count == 0) good = false;
		}

		// cout << srv << endl;

		if (good) {
			int wgt = 0;
			for (int srvr = 0; srvr < N; srvr++) {
				vector<string> st;

				for (int i=0; i<M; i++)
 					if (srv[i] == srvr) st.push_back(strs[i]);
 				// cout << "  > Server " << srvr << ": " << st << " wgt: " << calc(st) << endl;
 				wgt += calc(st);
			}
			++res[wgt];
		}

		int i=0;
		while (i<M && srv[i] == N-1) {
			srv[i] = 0;
			++i;
		}
		if (i<M) ++srv[i];
		else break;// fine
	}

	ii ans = *(res.rbegin());
	cout << "Case #" << testno << ": " << ans.first << " " << ans.second << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i=0; i<T; i++) {
		testcase(i+1);
	}
    return 0;
}