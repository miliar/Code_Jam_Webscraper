#include<bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef long long int LL;
typedef vector<int> VI;

#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define D double
#define LD long double
double EPS = 1e-12;

#define N 1123456

int bit[N];
VI sals;
VI vec[N], child[N];
vector< pair<int, pair<int,int> > > quer[N];
int maxs[N], mins[N];
int ans[N];

inline int query(int i){
	int ret = 0;
	while(i > 0){
		ret += bit[i];
		i -= (i & (-i));
	}
	return ret;
}

inline void update(int i){
	while(i < N){
		bit[i]++;
		i += (i & (-i));
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	sd(t);
	for(int cas = 1; cas <= t; cas++){
		int n, d;
		LL s, as, cs, rs, rm, m, am, cm;
		int ps, i, j, k, l, p, sz;
		cin>>n>>d;
		memset(bit, 0, sizeof bit);
		cin>>s>>as>>cs>>rs;
		cin>>m>>am>>cm>>rm;
		maxs[0] = s + 1;
		mins[0] = s + 1;
		sals.clear();
		sals.PB(s + 1);
		ps = s + 1;
		for(i = 0; i < n; i++){
			child[i].clear();
		}
		for(i = 1; i < n; i++){
			m = (m * am + cm) % rm;
			s = (s * as + cs) % rs;
			child[m % i].PB(i);
			maxs[i] = s + 1;
			mins[i] = s + 1;
			sals.PB(s + 1);
			//cout<<i<<" "<<s<<" "<<m % i<<endl;
		}
		for(i = 0; i < n - 1; ++i){
			for(j = (int)child[i].size() - 1; j >= 0; j--){
				k = child[i][j];
				maxs[k] = max(maxs[k], maxs[i]);
				mins[k] = min(mins[k], mins[i]);
			}
		}
		for(i = 1; i <= rs; i++){
			vec[i].clear();
			quer[i].clear();
		}
		for(i = 0; i < n; i++){
			vec[maxs[i]].PB(mins[i]);
			//cout<<i<<" "<<maxs[i]<<" "<<mins[i]<<endl;
		}
		sort(sals.begin(), sals.end());
		sals.erase(unique(sals.begin(), sals.end()), sals.end());
		sz = sals.size();
		j = 0;
		/*for(i = 0; i < sz; i++){
			cout<<sals[i]<<endl;
		}*/
		sals.PB(1123456789);
		for(i = 0; i < sz; i++){
			ans[i] = 0;
			while(j < sz){
				if(sals[j] - sals[i] > d){
					break;
				}
				j++;
			}
			if(ps < sals[i] || ps >= sals[j]){
				continue;
			}
			//cout<<sals[i]<<" "<<sals[j]<<endl;
			quer[sals[i] - 1].PB(MP(i, MP(sals[j - 1], -1)));
			quer[sals[i] - 1].PB(MP(i, MP(sals[i] - 1, 1)));
			quer[sals[j - 1]].PB(MP(i, MP(sals[j - 1], 1)));
			quer[sals[j - 1]].PB(MP(i, MP(sals[i] - 1, -1)));
		}
		for(i = 1; i <= rs; i++){
			for(j = (int)vec[i].size() - 1; j >= 0; j--){
				update(vec[i][j]);
			}
			for(j = (int)quer[i].size() - 1; j >= 0; j--){
				k = quer[i][j].S.F;
				l = quer[i][j].F;
				p = quer[i][j].S.S;
				//cout<<i<<" "<<k<<" "<<query(k)<<endl;
				if(p == 1){
					ans[l] += query(k);
				}
				else{
					ans[l] -= query(k);
				}
			}
		}
		int fans = 0;
		for(i = 0; i < sz; i++){
			fans = max(fans, ans[i]);
		}
		printf("Case #%d: %d\n", cas, fans);
	}
	return 0;
}

