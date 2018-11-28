#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;

	int a, b, k;
	for(int i = 0; i < t; i++) {
		cin >> a >> b >> k;

		int cnt = 0;
		for(int x = 0; x < a; x++)
		for(int y = 0; y < b; y++)
			if((x&y) < k) cnt++;

		cout << "Case #" << (i+1) << ": " << cnt << endl;
	}

	return 0;
}
