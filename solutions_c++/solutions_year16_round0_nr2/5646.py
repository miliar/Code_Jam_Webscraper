#include <iostream>
#include <string>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	string in;
	for (int i = 1; i <= n; ++i) {
		cin >> in;
		int result = 0;
		int size = in.length();
		for (int j = 0; j < size - 1; ++j) {
			if (in[j] != in[j + 1]) result++;
		}
		if (in[size-1] == '-') result++;
		cout << "Case #" << i << ": " << result << '\n';
	}


	return 0;
}