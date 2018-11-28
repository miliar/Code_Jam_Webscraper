#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int z = 1; z <= t; z++) {
	int smax;
	string str;
	cin >> smax >> str;

	int cur = 0, ans = 0;
	for (int i = 0; i <= smax; i++) {
	    if (cur < i) {
		ans += i - cur;
		cur = i;
	    }

	    cur += str[i] - '0';
	}
	cout << "Case #" << z << ": " << ans << endl;
    }
}
