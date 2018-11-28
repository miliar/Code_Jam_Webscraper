#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <map>
#include <stack>
#include <algorithm>
#include <climits>
#include <queue>
#include <cstdio>
#include <fstream>
#include <cstring>
#include <string>
#include <sstream>
#include <cassert>
using namespace std;
void main2();
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define all(x) (x).begin(),(x).end()
#if ( ( _WIN32 || __WIN32__ ) && __cplusplus < 201103L)
#define lld "%I64d"
#else
#define lld "%lld"
#endif
typedef long double ld;
inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }
typedef long long ll;


int main() {
#ifdef SHERLORE
	freopen("C:\\cygwin64\\home\\orzzzl\\uva\\in", "r", stdin);
	freopen("C:\\cygwin64\\home\\orzzzl\\uva\\out", "w", stdout);
#endif
	int tests = 1;
	scanf("%d", &tests);
	//pre();
	for (int i = 1; i <= tests; i++) {
#ifdef SHERLORE
		printf("Case #%d: ", i);
		ld stime = gett();
#endif
		main2();
#ifdef SHERLORE
		cerr << "Time: " << gett() - stime << endl;
#endif
	}
}

void main2() {
	int N;
	cin >> N;
	map<int, int> cnt;
	for (int i = 0; i < 2 * N - 1; i++) {
		int tmp;
		for (int i = 0; i < N; i++) {
			scanf("%d", &tmp);
			cnt[tmp]++;
		}

	}
	set<int> st;
	for (auto ele : cnt) {
		if (ele.second % 2 == 1) st.insert(ele.first);
	}
	assert(st.size() == N);
	for (auto ele : st) {
		cout << ele << ' ';
	}
	cout << endl;
}