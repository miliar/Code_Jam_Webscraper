#include <bits/stdc++.h>
using namespace std;

int tab[10010];

int main () {
	string s;
	int t, n;
	cin >> t;
	for (int p=1; p<=t; p++)  {
		cin >> n >> s;
		tab[0]=s[0]-'0';
		//cout << tab[0] << "\n";
		for (int i=1; i<=n; i++) {
			tab[i]=tab[i-1]+s[i]-'0';
		}
		int res=0;
		for (int i=1; i<=n; i++) {
			res= max (res, i-tab[i-1]);
		}
		//for (int i=0; i<=n; i++) cout << tab[i] << " ";
		//cout << "\n";
		cout << "case #" << p << ": " << res << "\n";
		for (int i=0; i<=n; i++) tab[i]=0;
	}
}