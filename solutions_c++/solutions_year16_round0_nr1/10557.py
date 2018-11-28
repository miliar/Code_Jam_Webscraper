#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;

void update(set<int> & digits, ull n) {
	string ns = to_string(n);
	for (char c : ns) {
		digits.insert(c - '0');	
	}
}

void print(int i, string ans) {
	cout << "Case #" <<  (i + 1) << ": " << ans << "\n";
} 
		
int main() {
	ios_base::sync_with_stdio(false); 
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		set<int> numset;
		set<int> digits;
		ull N, M; cin >> N; M = N;
		bool flag = true;	
		int j = 1;

		if (N == 0) {
			print(i, "INSOMNIA");
			continue;
		}
		while (flag) {
			update(digits, M);
			if (digits.size() > 9) {
				print(i, to_string(M));
				flag = false;
				continue;
			}
			j++;
			M = j * N;
		}
	}
	return 0;

}
