#include <stdio.h>
#include <string>
#include <cstring>

using namespace std;
char s[1005];


void solve() {
	scanf("%s", s);
	int l = strlen(s);
	string t = "";
	t = s[0];
	for (int i = 1; i < l; i++) {
		if (t[0] <= s[i])
			t = s[i] + t;
		else
			t = t + s[i];
	}
	printf("%s\n", t.c_str());
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		printf("Case #%d: ", R);
		solve();
	}

}