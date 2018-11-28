#include <iostream>
#include <cstring>
using namespace std;

char mark[10];

int main() {
	int N;
	cin >> N;
	for (int c = 1; c <= N; ++c) {
		memset(mark, 0, sizeof(mark));
		int s;
		cin >> s;
		cout << "Case #" << c << ": ";
		if (!s)
			cout << "INSOMNIA"<< endl;
		else {
			int cnt = 0;
			int r = -1;
			for (int i = 1; i <= 100; ++i) {
				int t = s * i;
				while (t) {
					if (!mark[t%10]) {
						mark[t%10] = 1;
						++cnt;
					}
					t /= 10;
				}
				if (cnt == 10) {
					r = i;
					break;
				}
			}
			if (r == -1)
				cerr << "Error" << endl;
			else
				cout << s*r << endl;
		}
	}
	return 0;
}
