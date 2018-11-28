#include <iostream>
#include <cassert>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main(int const argc, char const* const* const argv)
{
	int T;
	cin >> T;
	
	for (int i = 1; i <= T; ++i) {
		int N;
		cin >> N;
		string a, b;
		cin >> a >> b;
		int r = 0;
		bool fegla = false;
		while(a.size() && b.size()) {
			if (a[0] != b[0]) {
				fegla = true;
			}
			int i = 0, j = 0;
			for (; a[i] == a[0]; ++i);
			for (; b[j] == b[0]; ++j);
			--i;
			--j;
			r += abs(i - j);
			a = string(a.begin() + i + 1, a.end());
			b = string(b.begin() + j + 1, b.end());
		}
		if (fegla || a.size() || b.size()) {
			cout << "Case #" << i << ": Fegla Won" << endl;
		} else {
			cout << "Case #" << i << ": " << r << endl;
		}
	}
	return 0;
}

