#include <cstdio>
#include <iostream>

using namespace std;

void solve()
{
	int check[17] = {0, };

	for(int i = 0; i < 2; ++i) {
		int r;
		cin >> r;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				int x;
				cin >> x;
				if(j != r-1) check[x] = 1;
			}
		}
	}

	int sol = -1;

	for(int i = 1; i <= 16; ++i) {
		if(check[i] == 0) {
			if(sol == -1) sol = i;
			else {
				cout << "Bad magician!" << endl;
				return;
			}
		}
	}
	if(sol != -1) {
		cout << sol << endl;
		return;
	}
	cout << "Volunteer cheated!" << endl;

}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}