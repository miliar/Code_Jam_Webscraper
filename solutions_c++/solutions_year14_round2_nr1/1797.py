#include <iostream>
using namespace std;

int main()
{
	int t, N;
	string a, b;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int count = 0;
		cin >> N >> a >> b;
		int x = 0, y = 0;
		bool possible = true;
		
		while (x < a.length() && y < b.length()) {
				if (a[x] != b[y]) {
					possible = false;
					break;
				}
				char ch = a[x];
				int m = 0, n = 0;
				while (a[x] == ch && x < a.length()) {
					x++;
					m++;
				}
				while (b[y] == ch && y < b.length()) {
					y++;
					n++;
				}
				count += ((m-n > 0) ? m-n : n-m);
		}
		if (possible && x == a.length() && y == b.length())
			cout << "Case #" << i+1 << ": " << count << endl;
		else
			cout << "Case #" << i+1 << ": " << "Fegla Won" << endl;
	}
	return 0;
}