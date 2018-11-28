#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
	string s;
	for (int T=1; T<=t; T++) {
		cout << "Case #" << T << ": ";
		cin >> s;
		int ans=0;
		int r = s.length()-1;
		while (r>=0) {
			for (; r>=0; r--) if (s[r]=='-') break;
			if (r<0) break;
			if (s[0]=='+') {
				ans++;
				for (int i=0; ; i++) {
					if (s[i]=='-') break;
					else s[i]='-';
				}
			}
			ans++;
			string t="";
			for (int i=r; i>=0; i--) {
				if (s[i]=='+') t+='-';
				else t+='+';
			}
		//	cout << t << endl;
			s=t;
		}
		cout << ans << "\n";
	}
	return 0;
}
