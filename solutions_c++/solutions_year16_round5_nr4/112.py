#include <bits/stdc++.h>

using namespace std;

void doCase(int t) {
	int N, L;
	cin >> N >> L;
	
	vector<string> G(N);
	string B;
	
	for (int i=0; i<N; i++) cin >> G[i];
	cin >> B;
	
	for (int i=0; i<N; i++) {
		if (G[i] == B) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			return;
		}
	}
	
	if (L == 1) {
		cout << "Case #" << t << ": 0? 0" << endl;
	} else {
		cout << "Case #" << t << ": 10?";
		for (int i=1; i<L; i++) cout << "10";
		cout << " ";
		for (int i=1; i<L; i++) cout << "?";
		cout << endl;
	}
}

int main() {
	int T;
	cin>> T;
	for (int i=1; i<=T; i++) doCase(i);
	return 0;
}
