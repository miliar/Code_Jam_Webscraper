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

#define TASK "D"

int t, n, j;
    
string trans(long long x) {
 	string ret = "";

	while (x > 0) {
		ret += char(x % 2LL) + '0';
		x /= 2LL;
	}

	reverse(ret.begin(), ret.end());

	return ret;
}               
long long check(string s, long long base) {
 	long long val = 0LL, cur = 1LL;

	for (int i = (int)s.length() - 1; i >= 0; i--) {
	   	if (s[i] == '1') val += cur;
		cur *= base;
	}

	long long to = 1LL * sqrt(val);

	for (long long i = 2LL; i <= to; i++) {
	 	if (val % i == 0LL) {
	 	 	return i;
		}
	}

	return -1;
}  
void print(string s,vector<long long> &res) {
	cout << s;

	for (int i = 0; i < (int)res.size(); i++) cout << " " << res[i];

	cout << endl;
}                                              
int main() {
	#ifdef home
		freopen(TASK".in","r",stdin);
		freopen(TASK".out","w",stdout);
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0); 

	cin >> t;

	for (int k = 0; k < t; k++) {
		cin >> n >> j;

	 	cout << "Case #" << k + 1 << ":" << endl;

		for (long long i = (1LL << (n - 1)) + 1LL; j; i += 2LL) {
			vector<long long> vec;

			string s = trans(i);

		 	for (long long l = 2; l <= 10; l++) {
		 	 	vec.pb(check(s, l));
				if (vec.back() == -1LL) break;
			}	

			if (vec.back() == -1LL) continue;

			j--;
			print(s, vec);	
		}
	}
           
	#ifdef home
		eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
	#endif                                                                          
	return 0;
}