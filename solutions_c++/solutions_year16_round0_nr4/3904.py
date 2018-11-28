#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
int main() {
	int t, k, c, s;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> k >> c >> s;
		cout << "Case #" << i << ":";
		if(k != s) cout << " IMPOSSIBLE" << endl;
		for(int j = 1; j <= k; j++)
			cout << " " << j ;
		cout << endl;

	}
	return 0;
}