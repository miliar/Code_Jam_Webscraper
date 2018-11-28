#include <iostream>

using namespace std;

#define ULL unsigned long long

int main() {
	int t;
	cin >> t;
	
	for (int T = 1; T <= t; T++) {
		cout << "Case #" << T << ": ";
		
		ULL k, c, s;
		cin >> k >> c >> s;
		for (int i = 1; i <= k; i++)
			cout << i << " ";
		cout << "\n";
	}
	
	return 0;
}
