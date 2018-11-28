#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int count = 0;
	while (count++<n) {
		int a, b, k;
		int w = 0;
		cin >> a >> b >> k;
		for (int i=0; i<a; i++) {
			for (int j=0; j<b; j++) {
				if ((i & j) < k) {
					w++;
				}
			}
		}
		cout << "Case #" << count << ": " << w << endl;
	}
	return 0;
}