#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
	ifstream in("D-small-attempt1.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("D-small-attempt1.out");
	cout.rdbuf(out.rdbuf());
	// read
	string s;
	int kase = 1, T, K, C, S;
	cin >> T;
	while (T--) {
		cin >> K >> C >> S;
		cout << "Case #" << kase++ << ": ";
		if (K == 1) cout << 1;		
		else if (C == 1) {
			if (S < K) cout << "IMPOSSIBLE";
			else {
				for (int i = 1; i <= K; ++i) {
					cout << i;
					if (i != K) cout << ' ';
				}
			}
		} else {
			if (S < K/2) cout << "IMPOSSIBLE";
			else {
				S = K/2;
				for (int i = 0; i < S; ++i) {
					cout << 2*i*K + 2*(i + 1);
					if (i == 0 && K & 1) cout << ' ' << K;
					if (i + 1 != S) cout << ' ';
				}
			}
		}
		cout << endl;
	}
}