#include <iostream>
#include <vector>
#include <string>

using namespace std;

void main() {

	FILE *str, *abc;
	freopen_s(&str, "input.txt", "r", stdin);
	freopen_s(&abc, "out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << i + 1 << ": ";
		for (int i = 1; i <= s; i++)
			cout << i << " ";
		cout << endl;
	}
	

}