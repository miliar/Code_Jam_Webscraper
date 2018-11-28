#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000

bool good(string s) {
	for (char x: s)
		if (x=='-') return false;
	return true;
}

string flip(string s, int idx) {
	string ans = s;
	for (int i=idx-1;i>=0;--i)
		ans[idx-i-1] = s[i];
	for (int i=0;i<idx;++i)
		if (ans[i]=='+') {
			ans[i]='-';
		} else {
			ans[i]='+';
		}
	return ans;
}

int posi(string s) {
	int res = 0;
	while (s[res]=='+') res++;
	return res;
}

int negi(string s) {
	int res = 0;
	while (s[res]=='-') res++;
	return res;
}

ll solve(string s) {
	ll ans = 0;
	while (!good(s)) {
		int pos = posi(s);
		int neg = negi(s);
		if (neg > 0) {
			s = flip(s, neg);
			ans++;
		} else { // posi > 0
			s = flip(s, pos);
			ans++;
		}
	}
	return ans;

}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}

	return 0;
}