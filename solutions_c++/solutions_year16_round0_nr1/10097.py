#include<iostream>
#include<vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	int count = 1;
	while (t > 0) {
		int y;
		cin >> y;
		int mult = 2;
		if (y == 0) {
			cout << "Case #" << count << ": " << "INSOMNIA" << endl;
		}
		else {
			vector<bool> v(10);
			bool tottrue = false;
			for (int i = 0; i < v.size(); ++i) v[i] = false;
			int nomod = y;
			while (not tottrue) {
				int p = y;
				while (p > 0) {
					int r = p%10;
					v[r] = true;
					p = p/10;
				}
				bool res = false;
				for (int i = 0; i < v.size() and not res; ++i) {
					if (v[i] == false) {
						tottrue = false;
						res = true;
					}
					else tottrue = true;
				}
				y = nomod*mult;
				++mult;
			}
			cout << "Case #" << count << ": "<< y-nomod << endl;
		}
		++count;
		--t;
	}
}
