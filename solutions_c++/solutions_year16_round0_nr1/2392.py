#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	
	int tab[10];
	tab[0] = 1;
	for(int i = 0; i < 10; i++) {
		tab[i+1] = tab[i] << 1;
	}
	int allSeen = (tab[9] << 1)-1;

	int n;
	cin >> n;
	for(int i = 0; i < n; i++) {
		int x;
		cin >> x;
		if(x == 0) {
			cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
		}
		else {
			int seen = 0;
			int count = 1;
			int curr = x;
			while(seen != allSeen) {
				int analyseCurr = curr;
				while(analyseCurr != 0) {
					seen = seen | tab[analyseCurr%10];
					analyseCurr /= 10;
				}
				curr = curr+x;
			}
			cout << "Case #" << (i+1) << ": " << (curr-x) << endl;
		}
	}

	return 0;
}
