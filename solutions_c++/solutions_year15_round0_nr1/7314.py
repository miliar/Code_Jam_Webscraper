#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		int k;
		cin >> k;
		string s;
		cin >> s;
		int curr_clapping = 0;
		int need = 0;
		for (int j = 0; j <= k; ++j) {
			if (!j) { curr_clapping += (s[j] - '0'); continue; }
			if (curr_clapping < j) {
				need += (j - curr_clapping);
				curr_clapping = j + s[j] - '0';
			} else {
				curr_clapping += (s[j] - '0');
			}
		}
		cout << "Case #" << i << ": " << need << endl;
	}
}
