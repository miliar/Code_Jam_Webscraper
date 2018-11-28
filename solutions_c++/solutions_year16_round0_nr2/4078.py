#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen ("B-large-out.txt","w",stdout);

	int tc;
	char buf;
	cin >> tc;
	scanf("%c", &buf);
	for (int z = 1; z <= tc; z++) {
		int counter = -1;
		char prv = '0';
		char c = '0';
		while (1) {
			scanf("%c", &c);
			if (c == '\n') break;
			if (c != prv) counter++;
			prv = c;
		}
		if (prv == '-') counter++;


		printf("Case #%d: %d\n", z, counter);
	}

	
	return 0;
}
