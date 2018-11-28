#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T, t = 0, max, ans, now;
	string str;
	cin >> T;
	while (++t <= T) {
		ans = 0; now = 0;
		cin >> max >> str;
		for (size_t i = 0; i < str.size(); ++i) {
			if (max <= now) break;
			if (now < i && str[i] - '0' > 0) {
				ans += i - now;
				now += i + (str[i] - '0');
			} else now += str[i] - '0';
		}
		if (t > 1) cout << endl;
		cout << "Case #" << t << ": " << ans;
	}

    return 0;
}
