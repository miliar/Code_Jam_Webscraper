#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push

int t, n, pp, rr, ss, ut;
stack<int> vs[3];
string str[1<<13];
int main() {
	//freopen("a.in", "r", stdin);
	//freopen("a.out", "w", stdout);

	scanf("%d", &t);
	fo(_,1,t+1) {
		printf("Case #%d: ", _);
		scanf("%d %d %d %d", &n, &rr, &pp, &ss);
		fo(i,0,rr) vs[0].pb(i), str[i] = "R";
		fo(i,0,pp) vs[1].pb(i + rr), str[i + rr] = "P";
		fo(i,0,ss) vs[2].pb(i + rr + pp), str[i + rr + pp] = "S";
		ut = 1<<n;
		fo(i,0,n) {
			stack<int> nws[3];
			int r = vs[0].size(), p = vs[1].size(), s = vs[2].size(), mx = max(max(r, p), s);
			//printf("%d %d %d\n", r, p, s);
			if (mx > r + p + s - mx) {
				puts("IMPOSSIBLE"); break;
			}
			fo(j,0,1<<(n-i-1)) {
				int r = vs[0].size(), p = vs[1].size(), s = vs[2].size(), mx = max(max(r, p), s);
				if (r <= p && r <= s) { // p vs s
					int ppos = vs[1].top(), spos = vs[2].top();
					vs[1].pop(); vs[2].pop();
					string cand1 = str[ppos] + str[spos], cand2 = str[spos] + str[ppos];
					str[ut] = min(cand1, cand2);
					nws[2].push(ut++);
				} else if (p <= r && p <= s) { // r vs s
					int rpos = vs[0].top(), spos = vs[2].top();
					vs[0].pop(); vs[2].pop();
					string cand1 = str[rpos] + str[spos], cand2 = str[spos] + str[rpos];
					str[ut] = min(cand1, cand2);
					nws[0].push(ut++);
				} else { // r vs p
					int rpos = vs[0].top(), ppos = vs[1].top();
					vs[1].pop(); vs[0].pop();
					string cand1 = str[ppos] + str[rpos], cand2 = str[rpos] + str[ppos];
					str[ut] = min(cand1, cand2);
					nws[1].push(ut++);
				}
			}
			fo(j,0,3) vs[j] = nws[j];
		}
		if (ut == (1<<(n+1))-1) puts(str[ut-1].c_str());
		fo(i,0,3) while (!vs[i].empty()) vs[i].pop();
	}

	return 0;
}