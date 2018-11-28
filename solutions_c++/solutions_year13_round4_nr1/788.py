#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <utility>
#define MAX 1010
#define MOD 1000002013
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;

int comp[MAX];
map<ll, int> m;
piii st[MAX];
ll coord[2*MAX];
ll N;
int M;

void dfs(int x, int k){
	comp[x] = k;
	for(int i = 0; i < M; i++)
		if(comp[i] == -1 && st[i].x.x <= st[x].x.y)
			dfs(i, k);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		m.clear();
		scanf("%lld%d", &N, &M);
		set<ll> s;
		s.clear();
		for(int i = 0; i < M; i++){
			scanf("%d%d%d", &st[i].x.x, &st[i].x.y, &st[i].y);
			s.insert(st[i].x.x);
			s.insert(st[i].x.y);
		}
		set<ll>::iterator it = s.begin();
		for(int i = 0; it != s.end(); it++, i++){
			coord[i] = *it;
			m[*it] = i;
			//printf("%lld\n", *it);
		}
		for(int i = 0; i < M; i++){
			st[i].x.x = m[st[i].x.x];
			st[i].x.y = m[st[i].x.y];
		}
		for(int i = 0; i < M; i++)
			comp[i] = -1;
		sort(st, st+M);

		int k = 0;
		for(int i = 0; i < M; i++)
			if(comp[i] == -1){
				dfs(i, k);
				k++;
			}

		ll r = 0;
		for(int i = 0; i < M; i++){
			ll a, b;
			a = coord[st[i].x.x], b = coord[st[i].x.y];
			ll tmp = (2LL*N + 1) * (b - a) - (b - a) * (b - a);
			tmp /= 2LL;
			tmp = tmp % MOD;
			tmp = (tmp * st[i].y) % MOD;
			r = (r + tmp) % MOD;
		}
		for(int kk = 0; kk < k; kk++){
			ll qnto[2*MAX];
			for(int i = 0; i < 2*MAX; i++)
				qnto[i] = 0;
			for(int i = 0; i < M; i++)
				if(comp[i] == kk){
					qnto[st[i].x.y] += st[i].y;
				}
			for(int i = M-1; i >= 0; i--){
				if(comp[i] != kk)
					continue;
				for(int j = st[i].x.x; j < 2*MAX && st[i].y > 0; j++){
					ll q = min((ll)st[i].y, qnto[j]);
					ll a, b;
					a = coord[st[i].x.x], b = coord[j];
					ll tmp = (2LL*N + 1) * (b-a) - (b-a) * (b-a);
					tmp = tmp / 2LL;
					tmp = tmp % MOD;
					tmp = (tmp * q) % MOD;
					//printf(">%lld\n", tmp);
					r = (r - tmp + MOD) % MOD;
					st[i].y -= q;
					qnto[j] -= q;
				}

			}
		}
		printf("Case #%d: %lld\n", t, r);
	}
	return 0;
}
