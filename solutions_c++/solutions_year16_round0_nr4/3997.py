#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		__int64 K, C, S;
		cin >> K >> C >> S;
		__int64 d = 0, b = 1;
		for (int i = 0; i < C; i++) {
			d += b;
			b *= K;
		}

		cout << "Case #" << t + 1 << ":";
		for (int i = 0; i < K; i++) {
			cout << " " << i*d + 1;
		}
		cout << endl;
	}
	return 0;
}
