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

#define FOR(i,a,b) for(LL i=(a);i<(b);i += 2)
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

void print2base(LL n){
	string ret = "";
	while(n > 0){
		if(n & 1) ret = '1' + ret;
		else ret = '0' + ret;
		n >>= 1;
	}
	cout << ret << " ";
}

LL base(LL n, LL b){
	LL ret = 0, base = 1;
	//print2base(n);
	//cout <<  b << " ";
	while(n > 0){
		if((n & 1) != 0){
			ret += base;
		}
		base *= b;
		n >>= 1;
	}
	//cout << ret << endl;
	return ret;
}

LL div(LL n){
	LL ret = 0;
	for(LL i = 3; i * i < n; i += 2){
		if(n % i == 0){
			ret = i;
			break;
		}
	}
	return ret;
}


int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	int N, J;
	cin >> N >> J;

	cout << "Case #1:" << endl;

	int jNum = 0;
	FOR(i, (1LL << (N - 1)) + 1, 1LL << N){
		VI ret;
		FOR(j, 2, 11){
			LL tmp;
			tmp = div(base(i, j));
			if(tmp != 0){
				ret.push_back(tmp);
			}
			else{
				break;
			}
		}
		if(ret.size() < 9) continue;
		print2base(i);
		EACH(r, ret) cout << r << " ";
		cout << endl;
		jNum++;
		if(jNum == J) break;
	}

	return 0;
}
