#include <iostream>
#include <cstdio>
using namespace std;

int TAB[2502];

int main() {
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int n;
		cin >> n;
		
		for (int j = 0; j < 2502; j++) {
			TAB[j] = 0;
		}
		
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < 2 * n - 1; k++) {
				int pom;
				cin >> pom;
				TAB[pom]++;
			}
		}
		
		cout << "Case #" << i << ": ";
		
		for(int j = 1; j < 2502; j++) {
			if (TAB[j] % 2 != 0) {
				cout << j << " ";
			}
		}
		
		cout << endl;
	}
	
	return 0;
}
