#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

using namespace std;

int main() {

	int t, m, n;
	cin >> t;
	int c = 1;
	while (t--) {
		cin >> n >> m;
		int arr[n][m];
		for (int i = 0; i < n; i++) 
			for (int j = 0; j < m; j++)
				cin >> arr[i][j];
		bool flag = true;
		for (int i = 0; i < n && flag; i++){ 
			for (int j = 0; j < m && flag; j++){
				int x = arr[i][j];
				bool row = true;
				bool col = true;
				if (x > 100) {
					flag = false;
					break;
				}
				for (int k = 0; k < m && row; k++)
					if (arr[i][k] > x)
						row = false;
				for (int k = 0; k < n && col; k++)
					if (arr[k][j] > x)
						col = false;
				flag = row || col;
			}
		}
		string out = flag? "YES" : "NO";
		cout << "Case #" << c << ": " << out << endl;
		c++;
	}


}