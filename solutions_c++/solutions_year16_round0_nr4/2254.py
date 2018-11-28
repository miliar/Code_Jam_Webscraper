#include<iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int caso = 1; caso<=t;caso++) {
		cout << "Case #" << caso << ":";
		int k,c,s;
		cin >> k >> c >> s;
		if (k==1) {
			cout << " 1" << endl;
			continue;
		}
		if (c==1) {
			if(s<k) {
				cout << " IMPOSSIBLE" << endl;
				continue;
			}
			for(int i=1;i<=k;i++) {
				cout << " " << i;
			}
			cout << endl;
			continue;
		}
		int m = (k+1)/2;
		if (s < m) {
			cout << " IMPOSSIBLE" << endl;
			continue;
		}
		int i=2;
		while(m--) {
			cout << " " << i;
			i += 2*k+2;
			if(m==1 && (k%2)==1)i--;
		}
		cout << endl;
	}
	return 0;
}
