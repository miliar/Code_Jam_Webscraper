#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std; 
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1<<29;
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }

/////////////////////////////////////////////////////////////////////

char Str[1000];

int main()
{
	int T;
	scanf("%d", &T);

	int t = 1;
	while(T--) {
		scanf("%s", Str);
		string str = string(Str);
		reverse(str.begin(), str.end());

		//cout<<"str => " << str << "\n";

		int len = str.size();
		int ans = 0;
		for(int i = 0; i < len; ++i) {
			if(str[i] == '-') {
				ans++;
				for(int j = i; j < len; ++j) {
					if(str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
			}
		}

		printf("Case #%d: %d\n", t++, ans);
	}
    return 0;
}  

