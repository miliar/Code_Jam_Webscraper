#include <iostream>
#include <set>

using namespace std;
set<int> s;

void input_set(int n, set<int> &s) {
	while (n > 0) {
		int temp = n % 10;
		s.insert(temp);
		n /= 10;
	}
}

int main() {
	int t; cin >> t;
	for (int a0 = 0; a0 < t; ++a0) {
		int n; cin >> n;
		s.clear();
		if (n == 0) {
			cout << "Case #" << a0 + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		for (int i = 1; ; ++i) {
			input_set(i*n, s);
			if (s.size() == 10) {
				cout << "Case #" << a0 + 1 << ": " << i * n << endl;
				break;
			}
		}
	}
		
	return 0;
}