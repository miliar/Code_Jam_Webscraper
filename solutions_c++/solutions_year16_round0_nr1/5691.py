#include <iostream>
#include <set>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		long long n;
		cin >> n;
		set <int> digits;
		long long answer = -1;
		for (int i = 1; i < 101; ++i) {
			long long a = n * i;
			while (a) {
				digits.insert(a % 10);
				a /= 10;
			}
			if (digits.size() == 10) {
				answer = n * i;
				break;
			}
		}
		if (answer != -1) {
			cout << "Case #" << t + 1 << ": " << answer << endl;
		} else {
			cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
		}
	}
	return 0;
}