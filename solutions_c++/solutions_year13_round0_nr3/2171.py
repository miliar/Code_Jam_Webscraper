#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	vector<long long> palindromes;	// below sqrt(10^7)
	for (int i = 1; i < 10; i++) palindromes.push_back(i);
	for (int i = 1; i < 3163; i++) {
		int j = i;
		// test if palindrome
		int n = 0;
		int mod = 1;
		while (j > 0) {
			n = 10 * n + (j % 10);
			j /= 10;
			mod *= 10;
		}
		int joint = i * mod + n;
		palindromes.push_back(joint);
	}
	// test if squares are palindromes
	vector<long long> sqPalin;
	for (int i = 0; i < palindromes.size(); i++) {
		long long v = palindromes[i] * palindromes[i];
		// test if palin
		long long k = v;
		long long m = 0;
		while (k > 0) {
			m = 10 * m + (k % 10);
			k /= 10;
		}
		if (m == v) {
			sqPalin.push_back(v);
			//cout << v << " from " << palindromes[i] << "\n";
		}
	}
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		long long A, B;
		cin >> A >> B;
		int cnt = 0;
		for (int i = 0; i < sqPalin.size(); i++) {
			if (sqPalin[i] >= A && sqPalin[i] <= B) cnt++;
		}
		cout << "Case #" << (t+1) << ": " << cnt << "\n";
	}
	return 0;
}