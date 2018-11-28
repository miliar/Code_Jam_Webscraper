#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <complex>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define LLD "%lld"
#else
#define eprintf(...) 42
#define LLD "%I64d"
#endif
#define next _next
#define prev _prev
#define rank _rank
#define link _link
#define hash _hash

typedef long long ll;
typedef long long llong;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef complex <double> tc;

const double eps = 1e-9;
const double pi = 4 * atan(double(1));
const int base = int(1e4);

struct big{
	int a[100];
	
	big(){}
	
	big(int b){
		if(b == 0){
			a[0] = 1;
			a[1] = 0;
			return;
		}
		a[0] = 0;
		while(b > 0){
			a[++a[0]] = b % base;
			b /= base;
		}
	}
	
	big(string s){
		int k = sz(s) / 4, l = 4;
		if(sz(s) % 4 != 0){
			k++;
			l = sz(s) % 4;
		}
		a[0] = k;
		for(int i = 1; i <= a[0]; i++){
			a[i] = 0;
		}
		for(int i = 0; i < sz(s); i++){
			a[k] = a[k] * 10 + s[i] - '0';
			l--;
			if(l == 0){
				k--;
				l = 4;
			}
		}
	}
	
	void norm(){
		while(a[0] > 1 && a[a[0]] == 0){
			a[0]--;
		}
	}
	
};

big operator * (big a, big b){
	big c;
	c.a[0] = a.a[0] + b.a[0];
	for(int i = 1; i <= c.a[0]; i++){
		c.a[i] = 0;
	}
	for(int i = 1; i <= a.a[0]; i++){
		for(int j = 1; j <= b.a[0]; j++){
			c.a[i + j - 1] += a.a[i] * b.a[j];
			c.a[i + j] += c.a[i + j - 1] / base;
			c.a[i + j - 1] %= base;
		}
	}
	c.norm();
	return c;
}

inline int cmp(big a, big b){
	if(a.a[0] < b.a[0]){
		return -1;
	}
	if(a.a[0] > b.a[0]){
		return 1;
	}
	int i = a.a[0];
	while(i > 0 && a.a[i] == b.a[i]){
		i--;
	}
	if(i == 0){
		return 0;
	}
	if(a.a[i] < b.a[i]){
		return -1;
	}
	return 1;
}

bool operator == (big a, big b){
	return cmp(a, b) == 0;
}

bool operator < (big a, big b){
	return cmp(a, b) < 0;
}

bool operator <= (big a, big b){
	return cmp(a, b) <= 0;
}

big operator + (big a, big b){
	if(a.a[0] < b.a[0]){
		for(int i = a.a[0] + 1; i <= b.a[0]; i++){
			a.a[i] = 0;
		}
		a.a[0] = b.a[0];
	}	
	if(a.a[0] > b.a[0]){
		for(int i = b.a[0] + 1; i <= a.a[0]; i++){
			b.a[i] = 0;
		}
	}
	int ost = 0;
	for(int i = 1; i <= a.a[0]; i++){
		a.a[i] += b.a[i] + ost;
		if(a.a[i] >= base){
			a.a[i] -= base;
			ost = 1;
			continue;
		}
		ost = 0;
	}
	if(ost > 0){
		a.a[++a.a[0]] = 1;
	}
	return a;
}

big inf;
vector <string> ans;

inline void solve(int test){
	printf("Case #%d: ", test);
	string a, b;
	cin >> a >> b;
	big A(a), B(b);
	int res = 0;
	for(int i = 0; i < sz(ans); i++){
		big cur = big(ans[i]);
		if(A <= cur && cur <= B){
			res++;
		}
	}
	printf("%d\n", res);
}

inline string get(int a, int b){
	string res = "";
	if(a == 0){
		res = "0";
	}
	else{
		while(a > 0){
			res.pb('0' + a % 10);
			a /= 10;
		}
	}
	while(sz(res) < b){
		res += "0";
	}
	reverse(res.begin(), res.end());
	return res;
}

inline string get(big a){
	string res = get(a.a[a.a[0]], -1);
	for(int i = a.a[0] - 1; i > 0; i--){
		res += get(a.a[i], 4);
	}
	return res;
}

inline bool check(big a){
	if(inf < a){
		return false;
	}
	string res = get(a);
	int i = 0, j = sz(res) - 1;
	while(i < j){
		if(res[i] != res[j]){
			return false;
		}
		i++;
		j--;
	}
	return true;
}

inline bool check1(big a){
	string s = get(a), rs = s;
	reverse(rs.begin(), rs.end());
	string res = s + rs.substr(1, sz(rs) - 1);
	a = big(res);
	return check(a * a);
}

inline void write1(big a){
	string s = get(a), rs = s;
	reverse(rs.begin(), rs.end());
	string res = s + rs.substr(1, sz(rs) - 1);
	//cerr << "add1 " << res << endl;
	a = big(res);
	ans.pb(get(a * a));
	//cerr << "add1! " << ans.back() << endl;
}

inline bool check2(big a){
	string s = get(a), rs = s;
	reverse(rs.begin(), rs.end());
	string res = s + rs;
	a = big(res);
	return check(a * a);
}

inline void write2(big a){
	string s = get(a), rs = s;
	reverse(rs.begin(), rs.end());
	string res = s + rs;
	//cerr << "add " << res << endl;
	a = big(res);
	ans.pb(get(a * a));
	//cerr << "add! " << ans.back() << endl;
}

inline void dbg(big cur){
	string res = get(cur);
	cerr << "cur = " << res << endl;
}

void gen(big cur){
	//dbg(cur);
	for(int i = (cur == big(0)); i <= 2; i++){
		big ncur = cur * big(10) + big(i);
		if(check1(ncur)){
			write1(ncur);
		}
		if(check2(ncur)){
			write2(ncur);
			gen(ncur);
		}
	}
}

inline bool cmp_s(string a, string b){
	if(sz(a) != sz(b)){
		return sz(a) < sz(b);
	}
	return a < b;
}

inline bool check(ll a){
	string res = "";
	while(a > 0){
		res.pb('0' + a % 10);
		a /= 10;
	}
	int i = 0, j = sz(res) - 1;
	while(i < j){
		if(res[i] != res[j]){
			return false;
		}
		i++;
		j--;
	}
	return true;
}

int main(int argc, char **argv){
	if(argc > 1){
		freopen(argv[1], "r", stdin);
		freopen("ans.txt", "w", stdout);
	}
	else{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	inf = big(1);
	for(int i = 0; i < 100; i++){
		inf = inf * big(10);
	}
	gen(big(0));
	ans.pb("9");
	sort(ans.begin(), ans.end(), cmp_s);
	ans.resize(unique(ans.begin(), ans.end()) - ans.begin());
	cerr << "builded " << sz(ans) << endl;
	//return 0;
	/*for(int i = 0; i < sz(ans); i++){
		cout << ans[i] << endl;
	}
	cout << endl;
	for(int i = 1; i <= int(1e7); i++){
		if(check(i) && check(ll(i) * i)){
			cout << ll(i) * i << endl;
		}
	}
	return 0;*/
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		solve(i + 1);
		cerr << "test " << i << " of " << t << endl;
	}
	return 0;
}
