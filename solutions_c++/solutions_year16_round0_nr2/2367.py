#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		int l = int(s.size());
		int cnt = 0;
		for (int j = 1; j < l; j++) {
			if (s[j] != s[j - 1]) cnt++;
		}
		if (s.back() == '-') cnt++;
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
    return 0;
}

