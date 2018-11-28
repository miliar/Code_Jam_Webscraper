#include <bits/stdc++.h>
using namespace std;

int T, n;
char ori[1024];
string s;

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%s", ori);
		n = strlen(ori);
		s = "";
		for (int i = 0; i < n; ++i) {
			string tl, tr;
			tl = ori[i] + s;
			tr = s + ori[i];
			if (tl > tr)
				s = tl;
			else
				s = tr;
		}
		printf("%s\n", s.c_str());
	}
	return 0;
}