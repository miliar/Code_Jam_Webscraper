#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("input.in", "rt", stdin);
	freopen( "output.txt" , "wt" , stdout );
	int t, a, b;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> a;
		int temp, count = 0, res;
		bool vis[17];
		memset(vis, false, sizeof(vis));
		for (int j = 1; j <= 4; j++) {
			for (int k = 1; k <= 4; k++) {
				cin >> temp;
				if (j == a)
					vis[temp] = true;
			}
		}
		cin >> b;
		for (int j = 1; j <= 4; j++) {
			for (int k = 1; k <= 4; k++) {
				cin >> temp;
				if (j == b && vis[temp])
					count++, res = temp;
			}
		}
		cout << "Case #" << i << ": ";
		if (count == 1)
			cout << res << endl;
		else if (count == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}
