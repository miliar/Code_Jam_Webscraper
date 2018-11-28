#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for (int a = b; a < c; ++a)

int main() {
	int t, caso = 1;
	for (cin >> t; caso <= t; ++caso) {
		int a;
		map<int, int> q;
		cin >> a;
		fr(i,0,4) fr(j,0,4) {
			int x; cin >> x;
			if (a == i+1) q[x]++;
		}
		cin >> a;
		fr(i,0,4) fr(j,0,4) {
			int x; cin >> x;
			if (a == i+1) q[x]++;
		}
		int r = -1;
		fr(i,1,17) if (q[i] == 2 && r == -1) r = i; else if(q[i] == 2) r = -2;
		
		cout << "Case #" << caso << ": ";
		if (r > 0) cout << r << endl;
		else if (r == -1) cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;
	}
	return 0;
}
