#include <iostream>
#include <cstdio>
using namespace std;

int main () {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t, s;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> s;
		int invite = 0, standing = 0;
		for (int i = 0; i <= s; i++) {
			char aux;
			cin >> aux;
			int audience = aux - '0';
			int newFriends = max(0, i - standing);
			invite += newFriends;
			standing += newFriends + audience;
		}
		cout << "Case #" << tc << ": " << invite << endl;
	}
	return 0;
}
