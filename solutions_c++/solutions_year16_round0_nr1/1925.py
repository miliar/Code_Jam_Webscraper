#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		int n;
		cin >> n;
		
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		} else {
			vector<bool> d(10, false);
			int rd = 10, j = 0;
			
			while (rd > 0) {
				++j;
				int m = j * n;
				
				while (m > 0) {
					if (!d[m % 10]) {
						d[m % 10] = true;
						--rd;
					}
					m /= 10;
				}
			}
			
			cout << "Case #" << i << ": " << j * n << endl;
		}
	}
	
	return 0;
}