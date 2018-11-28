#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
 
using namespace std;
 
#define For(i,l,r) for (i = l; i <= r; i++)
#define FOR(i, n) for (int i = 0; i < n; i++)
#define for1(i,n) for (int i = 1; i <= n; i++)

int a[4][4], b[4][4];
int v[17];
int test_count, x, y;
int ans;

void init() {
	for1(i,16) v[i] = 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> test_count;

	for1(t, test_count) {
		init();
		cin >> x; x--;
		FOR(i, 4) FOR(j, 4) cin >> a[i][j];
		cin >> y; y--;
		FOR(i, 4) FOR(j, 4) cin >> b[i][j];
		FOR(i,4) v[a[x][i]]++;
		FOR(i,4) v[b[y][i]]++;
		ans = 0;
		for1(i,16) if (v[i] == 2) ans = (ans==0 ? i : -1);

		cout << "Case #" << t << ": ";
		if (ans == -1) cout << "Bad magician!";
		else if (ans == 0) cout << "Volunteer cheated!";
		else cout << ans;
		cout << endl;
	}


	//system("PAUSE");
	return 0;
}