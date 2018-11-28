# include <iostream>
# include <vector>

using namespace std;

int lastno(int &z) {
	int n = 10, ans, temp, k = z;
	std::vector<bool> a(10, false);
	while (n) {// until all numbers reached
		temp = k;
		while (true) { // check ofr each didgit
			if (temp) {
				if (!a[temp % 10]) {
					a[temp % 10] = true;
					n--;
				}
			}
			else {
				break;
			}
			temp = temp / 10;
		}

		if (n) {
			k = k + z;
		}
		else {
			break;
		}
	}

	return k;

}

int main() {

	int n, k;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> k;

		if (k == 0) {
			cout << "CASE #" << (i + 1) << ": INSOMNIA" << endl;
			continue;
		}
		int ans = lastno(k);
		cout << "CASE #" << (i + 1) << ": " << ans << endl;
	}
}