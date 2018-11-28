#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << t + 1 << ": ";
		for (int i = 1; i < s; ++i) {
			cout << i << ' ';
		}
		cout << s << endl;
	}
	return 0;
}