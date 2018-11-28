#include <algorithm> 
#include <iostream> 
#include <valarray> 
#include <iomanip> 
#include <fstream> 
#include <sstream> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <complex> 
#include <cstdio> 
#include <string> 
#include <vector> 
#include <bitset> 
#include <ctime> 
#include <cmath> 
#include <queue> 
#include <stack> 
#include <deque> 
#include <map> 
#include <set> 

using namespace std; 

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i) 
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i) 
#define error(x) cout << #x << " = " << (x) << endl; 
#define all(n) (n).begin(), (n).end() 
#define Size(n) ((int)(n).size()) 
#define mk make_pair 
#define pb push_back 
#define F first 
#define S second 
//#define X real() 
//#define Y imag() 

int _;
#define scanf _ = scanf

typedef long long ll; 
typedef pair<int, int> pii; 
typedef pair<ll, ll> pll; 
typedef complex<double> point; 

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; } 
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; } 
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); } 

bool ok(const basic_string<int> &str) {
	basic_string<int> res(2*Size(str), 0);
	FOR(i, 0, Size(str)) if (str[i]) FOR(j, 0, Size(str)) if (str[j]) {
		res[i+j] += str[i]*str[j];
		if (res[i+j] > 9) return false;
	}
	return true;
}

string p2(basic_string<int> num) {
	reverse(all(num));
	basic_string<int> res(Size(num)*2, 0);
	FOR(i, 0, Size(num)) FOR(j, 0, Size(num)) res[i+j] += num[i]*num[j];
	FOR(i, 0, Size(res)-1) res[i+1] += res[i]/10, res[i] %= 10;
	while (Size(res) > 0 && res[Size(res)-1] == 0) res.resize(Size(res)-1);
	reverse(all(res));
	string out;
	FOR(i, 0, Size(res)) out += char(res[i]+'0');
	return out;
}

string normalize(string s) {
	return string(128-Size(s), '0')+s;
}

vector<string> nums;

int len;
basic_string<int> str;

void go(int pos) {
	if (pos*2 >= len) {
		nums.pb(normalize(p2(str)));
		return;
	}
	FOR(i, pos?0:1, 3) {
		str[pos] = str[len-1-pos] = i;
		if (ok(str)) go(pos+1);
		str[pos] = str[len-1-pos] = 0;
	}
}

void gen(int len) {
	::len = len;
	str.resize(len);
	fill(all(str), 0);
	go(0);
}

int main() {
	nums.pb(normalize("1"));
	nums.pb(normalize("4"));
	nums.pb(normalize("9"));
	FOR(i, 2, 52) gen(i);
	int tc;
	cin >> tc;
	for (int l = 1; l <= tc; l++) {
		cout << "Case #" << l << ": ";
		string A, B;
		cin >> A >> B;
		cout << upper_bound(all(nums), normalize(B))-lower_bound(all(nums), normalize(A)) << endl;
	}
	return 0;
}

