#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		vector<char> c(N + 1);
		for (int n = 0; n < N + 1; n++) {
			cin >> c[n];
			c[n] -= '0';
		}
		vector<char> s(N, 0);
		int j = 0;
		for (int i = 0; i < N; i++) {
			if (j < i)
				j = i;
			for (int k = 0; k < c[i]; k++) {
				if (j < N)
					s[j++]++;
			}
		}
		int count = 0;
		for (int i = 0; i < N; i++)
			if (s[i] == 0)
				count++;
		cout << "Case #" << t << ": " << count << endl;
	}
}
