#include <iostream>
#include <cstdio>
using namespace std;
int lastNumber(int n) {
	bool exist[11];
	int i = 1;
	for (int j = 0; j < 10; j++) {
		exist[j] = false;
	}
	while (true) {
		int a = 0;
		int current = n*i;
		//cout << current << endl;
		while (true) {
			int k = current % 10;
			exist[k] = true;
			current = current / 10;
			if (current == 0) {
				break;
			}
		}
		for (int j = 0; j < 10; j++) {
			if (exist[j] == false) {
				a = 1;
			}
		}
		if (a == 0) {
			return n*i;
		}
		i++;
	}
}
int main() {
	freopen("a.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, a[300];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n; i++) {
		if (a[i] != 0) {
			cout << "Case #" << i + 1 << ": " << lastNumber(a[i]) << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		}
	}

}