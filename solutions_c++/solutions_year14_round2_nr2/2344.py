#include <cstdio>
#include <iostream>

using namespace std;

int a, b, k;

void read() {
	cin >> a >> b >> k;
}

void solve() {
	int total = 0;
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < b; j++) {
			if ((i & j) < k) {
				total++;
			}
		}
	}
	cout << total << endl;
}

int main() {
    freopen("inputB.in", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	
    int cases;
    cin >> cases;
    for (int count = 1; count <= cases; count++) {
		read();
        cout << "Case #" << count << ": ";
		solve();
    }
    return 0;
}