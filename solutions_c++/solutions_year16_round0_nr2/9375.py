#include <bits/stdc++.h>
#define sc1(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define sc3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define sc4(a, b, c, d) scanf("%d%d%d%d", &a, &b, &c, &d)
#define pb(a) push_back(a)
#define inf 0x3f3f3f3f
#define linf 0x3f3f3f3f3f3f3f3fLL
#define fr(i, a, n) for(int i = (a); (i) < (n); ++(i))
#define rp(a, b) fr(a, 0, b)
#define mp(a, b) make_pair(a, b)
#define st first
#define nd second
#define EPS 1e-8
#define clr(a, b) memset(a, b, sizeof(a))
#define addEdge(a, b) to[z] = b; ant[z] = adj[a]; adj[a] = z; z++

using namespace std;
typedef vector<int> vi;
typedef long long int ll;
typedef pair<int, int> pii;
const double PI = acos(-1);

int main() {
	string s;
	int caso = 0, t;
	sc1(t);
	
	while(t--) {
		caso++;
		cin >> s;
		ll ans = 0;
		while(true) {
			int idx = -1;
			string s2 = "";
			
			if(s[0] == '+') s2 += '-';
			else s2 += '+';
			
			fr(i, 1, s.length()) {
				if(s[i] == s[i-1]) {
					if(s[i] == '+') s2 += '-';
					else s2 += '+';
				}
				else {
					idx = i;
					break;
				}
			}
			if(idx == -1) {
				if(s2[0] == '-') break;
				idx = s.length();
			}
			
			s = s2 + s.substr(idx, s.length()-idx);			
			ans++;
		}
		
		printf("Case #%d: %lld\n", caso, ans);
	}

	return 0;
}




















