#include <iostream>
#include <unordered_set>
using namespace std;

void populate (int num, unordered_set<int>& SS) {
	if (num == 0) {
		return;
	}	
	SS.insert(num%10);
	populate (num/10, SS);
}

int main() {
	int T, N, R;
	cin >> T;
	unordered_set<int> S;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		cin >> N;
		R = N;
		if (N == 0) {
			cout << "INSOMNIA\n"; 
			continue;
		}
		while (true) {
			populate (R, S);
			if (S.size() == 10) {
				cout << R << "\n"; 
				break;
			}
			R += N;
		}
		S.clear();
	}
	return 0;
}