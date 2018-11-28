#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define mp make_pair
#define pb push_back
#define P 123456

int t, p;
pair<ll,ll> els[P]; ll curf[P];
vector<int> s;
map<int,int> vtoind;
int main() {
	freopen("d.in", "r", stdin); freopen("d.out", "w", stdout);
	scanf("%d", &t);
	fo(tc,1,t+1) {
		printf("Case #%d: ", tc);
		scanf("%d", &p);
		fo(i,0,p) scanf("%lld", &els[i].first);
		fo(i,0,p) scanf("%lld", &els[i].second);
		sort(els, els+p);
		s.clear(); vtoind.clear();
		fo(i,0,p) vtoind.insert(mp(els[i].first, i));
		fo(i,0,p) curf[i] = 0;
		curf[0] = 1;
		fo(i,0,p) while (curf[i] != els[i].second) {
			int nn = s.size();
			fo(j,0,1<<nn) {
				ll sum = els[i].first;
				fo(k,0,nn) if (j & (1<<k)) sum += s[k];
				curf[vtoind[sum]]++;
			}
			s.pb(els[i].first);
		}
		fo(i,0,s.size()) printf("%d%c", s[i], i+1 == s.size() ? '\n' : ' ');
	}

	return 0;
}