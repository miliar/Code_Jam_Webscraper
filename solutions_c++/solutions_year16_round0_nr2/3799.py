#include <iostream>
#include <vector>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b-l.out", "w", stdout);
	int n; cin >> n;
	for(int A=1; A<=n; A++) {
		string s; cin >> s;
		int ans = 0;
		for(int x=1; x<s.length(); x++) {
			if(s[x] != s[x-1]) ans++;
		}
		cout << "Case #" << A << ": " << ans+(s[s.length()-1]=='+'?0:1) << endl;
	}
}
