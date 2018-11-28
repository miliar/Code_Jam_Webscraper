#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
	int i, j, k;
	int rnds, cnt, result;
	int s, t, temp;
	char in;
	int a[2000];

	cin >> rnds;
	for (int ii = 0; ii < rnds; ii++) {
		cin >> s;
		result = 0;
		cnt = 0;
		getchar();
		for (int jj = 0; jj <= s; jj++) {
			in = getchar();
			a[jj] = in - 48;
		}
//		cout << "hehe: ";
		for (int jj = 0; jj <= s; jj++) {
			if (cnt < jj) {
				result += (jj - cnt);
				cnt += (jj - cnt);
			}
			cnt += a[jj];
//			cout << a[jj] << " ";

		}
//		cout << endl;
		cout << "Case #" << (ii + 1) << ": " << result << endl;
	}


	return 0;
}



