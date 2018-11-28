#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int t, i, c;
	char temp[1001];
	string s, res;

	scanf("%d", &t);

	c = 1;
	while (t--) {
		scanf("%s", temp);
		s = string(temp);
		res = s[0];
		for (i = 1; i < s.size(); i++) {
			if (res[0] <= s[i]) {
				res = s[i] + res;
			}
			else
				res = res + s[i];
		}
		cout << "Case #" << c << ": ";
		for (i = 0; i < res.size(); i++)
			cout << res[i];
		cout << endl;
		c++;
	}

	return 0;
}