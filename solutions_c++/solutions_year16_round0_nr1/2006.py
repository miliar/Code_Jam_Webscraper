#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]) {
	int testcases;
	cin >> testcases;
	for (int i = 1; i <= testcases; i++) {
		int n;
		cin >> n;
		vector<int> visited(10, 0);
		int count = 0, t = 1;;
		long res;
		for (t = 1; t < 100; t++) {
			res = n * t;
			long num = res;
			while (num > 0) {
				int digit = num % 10;
				if (!visited[digit]) {
					visited[digit] = 1;
					count ++;
				}
				num /= 10;
			}
			if (count == 10) {
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (count == 10) {
			cout << res << endl;
		} else cout << "INSOMNIA" << endl;
	}
	return 0;
}