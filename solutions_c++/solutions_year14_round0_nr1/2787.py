#include <fstream>
#include <map>

using namespace std;

ifstream cin("A-small-attempt0.in");
ofstream cout("output.txt");

void solve(int t) {
	int n1, n2;
	cin >> n1;
	map<int, int> p;
	int buf;
	for (int row = 1; row <= 4; ++row) {
		for (int i = 0; i < 4; ++i) {

			cin >> buf;
			if (row == n1) {
				p[buf]++;
			}
		}
	}
	cin >> n2;
	for (int row = 1; row <= 4; ++row) {
		for (int i = 0; i < 4; ++i) {

			cin >> buf;
			if (row == n2) {
				p[buf]++;
			}
		}
	}
	int num = 0, ans;
	for (int i = 1; i <= 16; ++i) {
		if (p[i] == 2) {
			num++;
			ans = i;
		}
	}
	if (num == 0) {
		cout << "Case #" << t << ": Volunteer cheated!" << endl;
	}
	if (num == 1) {
		cout << "Case #" << t << ": " << ans << endl;
	}
	if (num > 1) {
		cout << "Case #" << t << ": Bad magician!" << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		solve(i+1);
	}
	return 0;
}

