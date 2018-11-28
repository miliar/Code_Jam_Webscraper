#include <bits/stdc++.h>
using namespace std;
int solve() {
	int smax;
	cin >> smax;
	string s;
	cin >> s;
	int tot = 0, toAdd = 0;
	for(int i=0 ; i<smax ; i++) {
		int n = s[i]-'0';
		tot += n;
		if(tot<=i) {
			tot++;
			toAdd++;
		}
	}
	return toAdd;
}
int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int nbc;
	cin >> nbc;
	for(int i=1 ; i<=nbc ; i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
