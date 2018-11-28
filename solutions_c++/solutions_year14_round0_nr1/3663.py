#include <cstring>
#include <iostream>
using namespace std;

int vis[20];
int a[20];
int r;
int ans;

void deal()
{
	memset(vis, 0, sizeof(vis));

	cin >> r;
	for (int i = 0; i < 16; ++i) {
		cin >> a[i];
	}
	for (int i = (r - 1) << 2; i < r << 2; ++i) {
		++vis[a[i]];
//		cerr << i << ' ' << a[i] << endl;
	}

	cin >> r;
	for (int i = 0; i < 16; ++i) {
		cin >> a[i];
	}
	for (int i = (r - 1) << 2; i < r << 2; ++i) {
		++vis[a[i]];
//		cerr << i << ' ' << a[i] << endl;
	}

	ans = -1;
	for (int i = 1; i <= 16; ++i) {
		if (vis[i] > 1) {
			if (~ans) {
//				cerr << i << ' ' << ans << endl;
				cout << "Bad magician!" << endl;
				return;
			}
			else {
				ans = i;
			}
		}
	}
	if (~ans) {
		cout << ans << endl;
	}
	else {
		cout << "Volunteer cheated!" << endl;
	}
}

int main()
{
	int cases;

	ios::sync_with_stdio(false);

	cin >> cases;
	for (int t = 1; t <= cases; ++t) {
		cout << "Case #" << t << ": ";
		deal();
	}

	return 0;
}