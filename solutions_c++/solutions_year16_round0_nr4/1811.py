#include<iostream>

using namespace std;

int main() {
		
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	long long n;
	
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		int k,c,s;
		cin >> k >> c >> s;
		
		if(k == 1 && c > 0 && s > 0) {
			cout << "Case #" << i << ": 1" << endl;
			continue;
		}
		
		if(c == 1) {
			if(s <= k-1) {
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				continue;
			} else {
				cout << "Case #" << i << ": ";
				for(int j = 1; j <= k; j++) {
					cout << j << " ";
				}
				cout << endl;
				continue;
			}
		} else {
			if(s < k-1) {
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				continue;
			} else {
				cout << "Case #" << i << ": ";
				for(int j = 2; j <= k; j++) {
					cout << j << " ";
				}
				cout << endl;
				continue;
			}
		}
		
	}
	
	return 0;
}