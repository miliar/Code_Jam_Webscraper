#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int maxn = 1111;
const int mod = 1000002013;
int o[maxn] , e[maxn] , p[maxn];
int oo[maxn] , ee[maxn];
int x[maxn*2];
long long cnt[maxn*2];
int n , m;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T , cas = 1;
	scanf("%d",&T);
	while (T --) {
		scanf("%d%d",&n,&m);
		int index = 0;
		long long total = 0;
		for (int i = 0 ; i < m ; i ++) {
			scanf("%d%d%d",&o[i],&e[i],&p[i]);
			x[index++] = o[i];
			x[index++] = e[i];
			long long dis = e[i] - o[i];
			long long t = (n + n - dis + 1) * dis / 2;
			t %= mod;
			total += (t * p[i]) % mod;
			total %= mod;
		}
		sort(x , x + index);
		int mm = 1;
		for (int i = 1 ; i < 2 * m ; i ++) {
			if (x[i] != x[i - 1]) {
				x[mm++] = x[i];
			}
		}
		memset(cnt , 0 , sizeof(cnt));
		for (int i = 0 ; i < m ; i ++) {
			for (int j = 0 ; j < mm ; j ++) {
				if (o[i] == x[j]) {
					oo[i] = j;
				}
				if (e[i] == x[j]) {
					ee[i] = j;
				}
			}
			for (int j = oo[i] ; j < ee[i] ; j ++) {
				cnt[j] += p[i];
			}
		}
		long long sum = 0;
		for (int i = mm - 1; i >= 0 ; i --) {
			while (cnt[i]) {
				int e = i;
				int s = i;
				long long minp = cnt[i];
				for (int j = i - 1 ; j >= 0 ; j --) {
					if (cnt[j]) {
						minp = min(minp , cnt[j]);
						s = j;
					} else {
						break;
					}
				}
				for (int j = s ; j <= e ; j ++) {
					cnt[j] -= minp;
				}
				minp %= mod;
				long long dis = x[e+1] - x[s];
				long long t = (n + n - dis + 1) * dis / 2;
				t %= mod;
				sum += (t * minp) % mod;
				sum %= mod;
			}
		}
		long long ret = (total - sum + mod) % mod;
		cout << "Case #" << cas ++ << ": " << ret << endl;
	}
	return 0;
}