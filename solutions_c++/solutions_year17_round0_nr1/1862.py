#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
string S;
int a[1010];
int main() {
	int T, K;
	ofstream out("answer.txt");
	cin >> T;
	int i, j, t;
	int kase = 0, ans;
	bool ok;
	while (T--) {
		cin >> S >> K;
		for (i = 0; i < S.size(); i++) {
			if (S[i] == '-')
				a[i] = 1;
			else
				a[i] = 0;
		}
		ans = 0;
		t = S.size() - K;
		for (i = 0; i <= t; i++) {
			if (a[i]) {
				ans++;
				for (j = 0; j < K; j++)
					a[i + j] = 1 - a[i + j];
			}
		}
		ok = true;
		for (i = t + 1; i < S.size(); i++)
			if (a[i])
				ok = false;
		//printf("Case #%d: ", ++kase);
		out << "Case #" << (++kase)<<": ";
		if (ok) {
			//printf("%d\n", ans);
			out << ans << endl;
		} else {
			//printf("IMPOSSIBLE\n");
			out << "IMPOSSIBLE" << endl;
		}
	}
	out.close();
	return 0;
}
