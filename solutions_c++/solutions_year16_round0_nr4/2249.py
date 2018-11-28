#include <iostream>

using namespace std;

int main() {
	int T;
	int t = 1;
	int a, b, c;

	cin >> T;
	while (t <= T) {
		cin >> a >> b >> c;

		cout << "Case #" << t << ": ";

		for (int i = 1; i <= c; i++)
			cout << i << " ";
		cout << endl;
		t++;
	}
}