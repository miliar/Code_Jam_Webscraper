#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

typedef long long ll;

ifstream fin("input.txt"); ofstream fout("output.txt");
ll t, n, k;

ll getComposite(ll n) {
	ll ans = -1;
	for (ll i = 2; i * i <= n; i++) if (n % i == 0) ans = i;
	return ans;
}

void solve(string s) {
	int ans[11];

	for (int i = 2; i <= 10; i++) {
		ll a = 0, r = 1;
		for (int j = n - 1; j >= 0; j--) a += r * (s[j] - '0'), r *= i;
		ll c = getComposite(a);
		if (c == -1) return;
		ans[i] = c;
	}

	k--;
	fout << s << ' ';
	for (int i = 2; i <= 10; i++) fout << ans[i] << ' '; fout << endl;
}

void generateBinary(string s) {
	if (k < 1)  return;
		
	if (s.size() + 2 == n) {
		solve("1" + s + "1");
		return;
	}

	generateBinary(s + "0");
	generateBinary(s + "1");
}

int main() {
	fin >> t >> n >> k;
	fout << "Case #" << t << ":" << endl;
	generateBinary("");

	fin.close(); fout.close();
	return 0;
}