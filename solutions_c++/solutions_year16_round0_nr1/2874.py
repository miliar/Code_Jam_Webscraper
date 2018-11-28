#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef tuple<int, int, int> TIII;
typedef long long LL;
typedef unsigned long long ULL;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define MP make_pair
#define MT make_tuple
#define SZ(a) int((a).size())
#define EACH(i,c) for(auto i: c)
#define SORT(c) sort((c).begin(),(c).end())

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()

const double EPS = 1e-10;
const double PI  = acos(-1.0);

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

set<int> f(int n){
	set<int> ret;
	while(n > 0){
		ret.insert(n % 10);
		n /= 10;
	}
	return ret;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

#if 1
	int T;
	cin >> T;
	FOR(times, 1, T + 1){
		int N;
		cin >> N;
		cout << "Case #" << times << ": ";
		if(N == 0){
			cout << "INSOMNIA" << endl;
		}
		else{
			VI done(10, 0);
			FOR(i, 1, 1e6){
				auto S = f(N * i);
				EACH(s, S) done[s] = 1;
				bool ok = true;
				EACH(d, done) if(d == 0) ok = false;
				if(ok){
					cout << N * i << endl;
					break;
				}
			}
		}

	}
#else
	cout << 1000001 << endl;
	REP(i, 1e6 + 1){
		cout << i << endl;
	}

#endif
	return 0;
}
