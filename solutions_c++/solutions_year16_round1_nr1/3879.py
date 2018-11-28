#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main() {
	int n,kase=0; cin >> n; getchar();
	while (n--) {
		string s;
		char ans[1005],rans[1005];
		memset(ans, 0, sizeof(ans));
		memset(rans, 0, sizeof(rans));
		getline(cin, s);
		rans[0] = s[0];
		int acnt = 0, rcnt = 0;
		printf("Case #%d: ", ++kase);
		for (int i = 1; i < s.size(); i++) {
			if (s[i] < rans[rcnt]) ans[acnt++] = s[i];
			else rans[++rcnt] = s[i];
		}
		for (int i = rcnt; i >= 0; i--) {
			if (rans[i] != 0) cout << rans[i];
		}
		for (int i = 0; i < acnt; i++) {
			if (ans[i] != 0) cout << ans[i];
		}
		cout << endl;
	}
	//system("PAUSE");
	return 0;
}