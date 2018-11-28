#include <iostream>
#include <string>
using namespace std;
void cas() {
	int y = 0, a = 0, S; cin >> S;
	int v[1001]; char c;
	for (int s = 0; s <= S; ++s) {
		cin >> c; v[s] = c - '0';
	}
	//for (int s = 0; s <= S; ++s) cout << v[s];
	for (int s = 0; s <= S; ++s) {
		if (s > a) {
			y += s - a;
			a += s - a;
		}
		a += v[s];
	}
	cout << y << endl;
}
int main() {
	int t; cin >> t;
	int x = 1; while (t--) {
		cout << "Case #" << x++ << ": ";
		cas();
	}
}
