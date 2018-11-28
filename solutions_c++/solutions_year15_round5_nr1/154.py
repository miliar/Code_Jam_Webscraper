#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define mp make_pair
#define pb push_back
#define N 1234567

int t, n, d, ans, cnt;
ll gena, genb, genc, gend;
ll sal[N], par[N];
vector<int> al[N];
pair<int,int> ss[N];
char alive[N], con[N];
void gen(ll a, ll b, ll c, ll d, ll res[]) {
	res[0] = a;
	fo(i,1,n) res[i] = (res[i-1]*b + c)%d;
}
void add(int aid) {
	//printf("ADD %d\n", aid);
	alive[aid] = 1;
	if (aid == 0 || con[par[aid]]) con[aid] = 1;
	if (!con[aid]) return;
	//puts("CON");
	cnt++;
	//for (int i = 0; i < al[aid].size(); i++) if (alive[al[aid][i]] && !con[al[aid][i]]) add(al[aid][i]);
	for (int i = 0; i < al[aid].size(); i++) if (alive[al[aid][i]]) add(al[aid][i]);
}
void rem(int rid) {
	//printf("REM %d\n", rid);
	alive[rid] = 0;
	if (!con[rid]) return;
	//puts("CON");
	cnt--;
	for (int i = 0; i < al[rid].size(); i++) if (alive[al[rid][i]]) rem(al[rid][i]);
	con[rid] = 0;
}
int main() {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	scanf("%d", &t);
	fo(tc,1,t+1) {
		printf("Case #%d: ", tc);
		scanf("%d %d", &n, &d);
		scanf("%lld %lld %lld %lld", &gena, &genb, &genc, &gend);
		gen(gena, genb, genc, gend, sal);
		scanf("%lld %lld %lld %lld", &gena, &genb, &genc, &gend);
		gen(gena, genb, genc, gend, par);
		//fo(i,0,n) printf("%lld%c", sal[i], i==n-1 ? '\n' : ' ');
		fo(i,1,n) par[i] %= i;
		fo(i,0,n) al[i].clear();
		fo(i,1,n) al[par[i]].pb(i);
		fo(i,0,n) ss[i] = mp(sal[i], i);
		sort(ss, ss+n);
		fo(i,0,n) alive[i] = 0;
		fo(i,0,n) con[i] = 0;
		ans = 0; cnt = 0;
		int lut = 0, rut = 0;
		while (lut < n) {
			while (rut < n && sal[ss[rut].second] - sal[ss[lut].second] <= d) add(ss[rut++].second);
			//printf("%d %d %d %d %d %d %d\n", lut, ss[lut].first, ss[lut].second, rut, ss[rut].first, ss[rut].second, cnt);
			ans = max(ans, cnt);
			rem(ss[lut].second); lut++;
		}
		printf("%d\n", ans);
	}

	return 0;
}