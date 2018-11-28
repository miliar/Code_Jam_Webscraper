#include <iostream>
#include <vector>
using namespace std;

vector<int> f() {
	int tmp;
	int a; cin >> a;
	vector<int> as(4);
	for (int i = 1; i <= 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (i == a) cin >> as[j];
			else cin >> tmp;
		}
	}
	return as;
}

int g(vector<int> v1, vector<int> v2) {
	int ret = -1;
	for (int i = 0; i < v1.size(); i++) {
		for (int j = 0; j < v2.size(); j++) {
			if (v1[i] == v2[j]) {
				if (ret == -1) {
					ret = v1[i];
				} else if (ret > 0) {
					return 0;
				}
			}
		}
	}
	return ret;
}

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++)  {
		int ans = g(f(), f());
		cout << "Case #" << No << ": ";
		if (ans == -1) {
			cout << "Volunteer cheated!" << endl;
		} else if (ans == 0) {
			cout << "Bad magician!" << endl;
		} else {
			cout << ans << endl;
		}
	}
}
