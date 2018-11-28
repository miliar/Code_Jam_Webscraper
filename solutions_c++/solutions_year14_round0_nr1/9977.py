#include <bits/stdc++.h>

using namespace std;

int x, y;
int a[5][5], b[5][5];

void input () {
	cin >> x;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> a[i][j];

	cin >> y;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> b[i][j];
}

bool used[20];

void output () {
	memset (used, 0, sizeof used);

	for (int j = 0; j < 4; j++) {
		int i = x - 1;
		used[a[i][j]] = true;
	}

	int co = 0, d = -1;
	
	for (int j = 0; j < 4; j++) {
		int i = y - 1;

		if (used[b[i][j]]) {
			co++;
			d = b[i][j];
		}

		used[b[i][j]] = true;
	}
	if (!co)
		puts ("Volunteer cheated!");
	else
		if (co > 1)
			puts ("Bad magician!");
		else
			printf ("%d\n", d);
}

int main () {
	#ifdef _LOCAL
		freopen (".in", "r", stdin);
		freopen (".out", "w", stdout);
	#endif

	int t, Case = 1; cin >> t;

	while (t--) {
		input();

		printf ("Case #%d: ", Case++);

		output();
	}
	
	return 0;
}