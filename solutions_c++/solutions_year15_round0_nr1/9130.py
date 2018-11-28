#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,c,n,acum,extra;
	string s;

	scanf("%d", &t);

	c = t;

	while (t--) {
		scanf("%d", &n);
		acum = extra = 0;
		cin >> s;

		for (int i=0; i<=n; i++) {
			if (acum < i) {
				extra += i - acum;
				acum += i-acum;
				//cout << "extra: " << extra <<endl;
			}
			acum += s[i]-48;
			//cout << s[i]-48 << ", acum: " << acum << endl;
		}

		printf("Case #%d: %d\n", c-t, extra);
	}
}