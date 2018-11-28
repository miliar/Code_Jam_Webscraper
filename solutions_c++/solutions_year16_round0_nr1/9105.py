#include <iostream>
#include <set>

using namespace std;

set <int> s;

void add_to_set(int x) {
	while (x > 0) {
		s.insert(x % 10);
		x /= 10;
	}
}

int main() {
	int T, cnt = 0;
	cin >> T;
	while (T--) {
		int n;
		cin >> n;
		s.clear();
		cout << "Case #" << ++cnt << ": ";
		if (n == 0)
			cout << "INSOMNIA" << endl;
		else {
			for (int i = 1; ; i++) {
				add_to_set(i * n);
				if (s.size() == 10) {
					cout << i * n << endl;
					break;
				}
			}
		}	
	}
}
