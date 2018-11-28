#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
	freopen("out.txt", "w", stdout);
	freopen("in.in", "r", stdin);

	int T;
	cin >> T;

	int s_max; char buff; int i_buff;
	for (int i = 0; i < T; i++) {
		cin >> s_max;
		cin.get(buff); // space.
		int levantados = 0;
		int added = 0;
		for (int j = 0; j <= s_max; j++) {
			cin.get(buff);
			i_buff = buff - '0';
			if (levantados < j) {
				added += j - levantados;
				levantados += j - levantados;
			}
			levantados += i_buff;
		}
		cin.get(buff); // newline.
		cout << "Case #" << i + 1 << ": " << added << endl;
	}

	return 0;
}