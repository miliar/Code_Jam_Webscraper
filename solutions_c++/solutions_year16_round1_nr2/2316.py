#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("small-output.out", "w", stdout);
	
	int t;
	cin >> t;
	int m = t;
//	cout << t << endl;
	int i = 1;
	int heights[3000];
	while(i <= m) {
		for(int k = 0; k <= 3000; k++) {
			heights[k] = 0;
		}
		int n;
		cin >> n;
		int a[n + 10][n + 10];
		for(int k = 1; k <= 2*n-1; k++) {
			for(int l = 1; l <= n; l++) {
				cin >> a[k][l];
				heights[a[k][l]]++;
			}
		}
		int count = 0;
		int b[3000];
		for(int k = 1; k <= 3000; k++) {
			if(heights[k] % 2 == 1) {
				count++;
				b[count] = k;
			}
		}
		for(int k = 1; k <= count-1; k++) {
			for(int l = k + 1; l <= count; l++) {
				if(b[k] > b[l]) {
					int h = b[k];
					b[k] = b[l];
					b[l] = h;
				}
			}
		}
		
		i++;
		cout << "Case #" << i-1 << ": ";
		for(int k = 1; k <= count; k++) {
			cout << b[k] << " ";
		}
		cout << endl;
	}
	
	return 0;
}