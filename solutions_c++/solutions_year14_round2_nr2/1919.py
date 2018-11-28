#include <iostream>

using namespace std;

int main () {
	int t, ca;
	int a, b, k, cnt = 0;

	cin >> t;
	ca = 1;
	while (t--) {
		cnt = 0;
		cin >> a >> b >> k;

		for (int i = 0; i < a; ++i)
		{
			for (int j = 0; j < b; j++)
				if ((i&j) < k) cnt++;
		}

		cout << "Case #" << ca++ << ": " <<cnt << endl;
	}
}