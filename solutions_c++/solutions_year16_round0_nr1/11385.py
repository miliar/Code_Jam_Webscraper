#include <iostream>
#include <cstring>
using namespace std;

bool visited[10];
int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		memset(visited, false, sizeof visited);
		int a;
		cin >> a;
		long long val = -1;
		for (int i = 1; i <= 1000000 && val == -1; i++) {
			long long k = (i * a);
			for (int j = 0; j < 1 || k; j++) {
				visited[k % 10] = true;
				k /= 10;
			}
			bool ok = true;
			for (int j = 0; j < 10; j++)
				ok &= visited[j];

			if (ok)
				val = (i + 0LL) * a;
		}
		if (val == -1)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << t << ": " << val << endl;
	}
	return 0;
}