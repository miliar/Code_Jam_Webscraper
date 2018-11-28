#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int T = 0;
	char output = 0;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int n = 0;
		int m = 0;
		output = 1;
		cin >> n >> m;
		int height[n][m];
		int largestinrow[n];
		int largestincol[m];
		
		memset(height, 0, n*m*sizeof(int));
		memset(largestinrow, 0, n*sizeof(int));
		memset(largestincol, 0, m*sizeof(int));
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> height[i][j];
				if (height[i][j] > largestinrow[i])
					largestinrow[i] = height[i][j];
				if (height[i][j] > largestincol[j])
					largestincol[j] = height[i][j];
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (height[i][j] < largestinrow[i]) {
					if (height[i][j] < largestincol[j]) {
						output = 0;
					}
				}
				if (!output)
					break;
			}
			if (!output)
				break;
		}
		
		
		cout << "Case #" << t << ": ";
		if (output)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}