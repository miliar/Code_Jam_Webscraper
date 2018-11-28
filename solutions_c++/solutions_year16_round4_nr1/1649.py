#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <deque>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <climits>
#include <cctype>
#include <utility>
#include <cassert>
#include <ctime>
using namespace std;

#define ft first
#define sd second
#define pb push_back
#define endl '\n'
#define buli(x) __builtin_popcountll(x)
#define cpy(a,e) memcpy(a,e,sizeof(e))
#define clr(a,e) memset(a,e,sizeof(a))
#define iter(c) __typeof((c).begin())
#define tr(c,i) for (iter(c) i=(c).begin();i!=(c).end();i++)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define rep(i,n) for (int (i)=0;(i)<(n);i++)
#define repd(i,n) for (int (i)=(n)-1;(i)>=0;i--)
#define reps(i,s,e) for (int (i)=(s);(i)<=(e);i++)
#define repds(i,s,e) for (int (i)=(s);(i)>=(e);i--)
#define repl(i,s,e) for (int (i)=(s);(i);i=e[i])

#define TASK "A-small-attempt5"

int t, n;
int r, p, s;

// r p s

int f(int x, int y) {
 	vector<int> vec;

	vec.emplace_back(x);
	vec.emplace_back(y);

	sort(vec.begin(), vec.end());

	if (vec[0] == vec[1]) assert(false);

	if (vec[0] == 0) {
	 	if (vec[1] == 1) return 0;
	 	else return 2;
	} else return 1;
}
inline bool C(vector<int> vec) {
	vector<int> temp;

  	for (auto u : vec) temp.emplace_back(u);

  	while ((int)temp.size() > 1) {
  	 	for (int i = 0; i < (int)temp.size(); i += 2) {
  	 	 	if (temp[i] == temp[i + 1]) return false;
  	 	}

  	 	vector<int> v;

  	 	for (int i = 0; i < (int)temp.size(); i += 2) {
  	 	 	v.emplace_back(f(temp[i], temp[i + 1]));
  	 	}

  	 	temp.swap(v);
  	}                

  	return true;
}      
inline int diu(int x) {
 	if (x == 0) return 1;
	if (x == 1) return 0;
	if (x == 2) return 2;
}
int main() {
	#ifdef home
		freopen(TASK".in","r",stdin);
		freopen(TASK".out","w",stdout);
	#endif 
	ios::sync_with_stdio(false);

	cin >> t;

	for (int _t = 0; _t < t; _t++) {
	 	cin >> n >> r >> p >> s;
		vector<int> vec;

		for (int i = 0; i < r; i++) vec.emplace_back(1);
		for (int i = 0; i < p; i++) vec.emplace_back(0);
		for (int i = 0; i < s; i++) vec.emplace_back(2);

		sort(vec.begin(), vec.end());

		bool flag = false;

		vector<int> res;

		do {     
		     	if (C(vec)) {
		     	 	flag = true;
				break;		     	}
		} while (next_permutation(vec.begin(), vec.end()));

		cout << "Case #" << _t + 1 << ": ";

		if (!flag) cout << "IMPOSSIBLE" << endl;
		else {
		 	for (auto u : vec) {
		 	 	if (u == 1) cout << 'R';
		 	 	else if (u == 0) cout << 'P';
		 	 	else cout << 'S';
		 	}

		 	cout << endl;
		}
	}
           
	#ifdef home
		eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
	#endif                                                                          
	return 0;
}