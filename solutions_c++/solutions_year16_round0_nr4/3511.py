#include <iostream>
#include <vector>

using namespace std;

void getPosition(int k, int c, vector<unsigned long long> &arr) {
	unsigned long long len = 1;

	arr.clear();
	for (int i = 0; i < k; i ++) {
		arr.push_back(i + 1);
	}

	while (--c > 0) {
		len *= k;
		for (int i = 0; i < k; i ++) {
			arr[i] += i * len;
		}
	}
}

int main() {
	int t, T, k, c, s;
	vector<unsigned long long> arr;
	cin >> T;

	t = 0;
	while (T-- > 0) {
		cin >> k >> c >> s;
		cout << "Case #" << ++t << ": ";
		getPosition(k, c, arr);
		for (int i = 0; i < arr.size(); i ++) {
			cout << arr[i];
			if (i != arr.size() - 1) cout << " ";
		}
		cout << endl;
	}
	return 0;
}
