#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int n, r, p, s;
string ansr[13], ansp[13], anss[13];

string test(int n, string &ans) {
	int rr = 0, pp = 0, ss = 0;
	for (int i = 0; i < ans.length(); i++) {
		if (ans[i] == 'R') rr++;
		else if (ans[i] == 'P') pp++;
		else if (ans[i] == 'S') ss++;
	}
	if (r == rr && p == pp && s == ss) return ans;
	else return "Z";
}
int main() {
	ansr[0] = "R";
	ansp[0] = "P";
	anss[0] = "S";
	for (int i = 1; i <= 12; i++) {
		if (ansr[i - 1] < anss[i - 1]) ansr[i] = ansr[i - 1] + anss[i - 1];
		else ansr[i] = anss[i - 1] + ansr[i - 1];
		if (ansp[i - 1] < ansr[i - 1]) ansp[i] = ansp[i - 1] + ansr[i - 1];
		else ansp[i] = ansr[i - 1] + ansp[i - 1];
		if (anss[i - 1] < ansp[i - 1]) anss[i] = anss[i - 1] + ansp[i - 1];
		else anss[i] = ansp[i - 1] + anss[i - 1];
	}
	int t, tt;
	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++) {
		scanf("%d%d%d%d", &n, &r, &p, &s);
		vector<string> ans;
		ans.push_back(test(n, ansr[n]));
		ans.push_back(test(n, ansp[n]));
		ans.push_back(test(n, anss[n]));
		sort(ans.begin(), ans.end());
		if (ans[0] != "Z") printf("Case #%d: %s\n", tt, ans[0].c_str());
		else printf("Case #%d: %s\n", tt, "IMPOSSIBLE");
	}
	return 0;
}
