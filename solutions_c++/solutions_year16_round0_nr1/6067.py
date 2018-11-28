#include <bits/stdc++.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

#define all(x) (x).begin(), (x).end()

const int maxn = 2002;

set<int> alive, connect[maxn];
vector<PII> bulbs, bases;
VI e[maxn];
bool can[maxn][maxn];

int val(PII x, PII y, PII z) {
	int dx = y.first - x.first;
	int dy = y.second - x.second;
	int res = z.first * dy - z.second * dx + x.second * dx - x.first * dy;
	return res;
}
int litl[2005];
int litr[2005];

void flush() {
	alive.clear(); bulbs.clear(); bases.clear();
	for (int i = 0; i < maxn; ++i) {
		connect[i].clear();
		e[i].clear();
		litl[i]= 0;
		litr[i]= 0;
	}
}
#define S second
#define F first
int main() {
	//freopen("0.in","r",stdin);freopen("0.out","w",stdout);

	int T, N, L, R, H;
	scanf("%d", &T);
	while (T--) {
		flush();
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d %d %d", &L, &R, &H);
			bulbs.emplace_back(PII(L, H));
			bulbs.emplace_back(PII(R, H));

			bases.emplace_back(PII(L, 0));
			bases.emplace_back(PII(R, 0));
		}
		sort(all(bulbs));
		sort(all(bases));
		for (int i = 0; i < bulbs.size(); ++i) {
			for (int j = 0; j < bases.size(); ++j) {
				if (i == j) {
					can[i][j] = 1;
				} else {
					bool ok = 1;
					int st = min(i,j);
					int to = max(i,j);
					for (int k = st+1; k < to && ok; ++k) {
						if (val(bulbs[i], bases[j], bulbs[k]) * 1LL * val(bulbs[i], bases[j], PII(bases[j].first, bases[j].second - 1)) < 0) {
							ok = 0;
						}
					}
					can[i][j] = ok;
				}
			}
		}

		for(int i=0;i<N;++i){
			for(int j=0;j<N;++j){
				can[2*i][2*j] = can[2*i+1][2*j+1] = 0;
			}
			can[2*i][2*i+1] = can[2*i+1][2*i] = 0;
			can[2*i][2*i] = can[2*i+1][2*i+1] = 1;
		}

		litl[0] = 1;
		for(int i=1;i<N;++i){
			int ok = 0;
			for(int j=0;j<i;++j){
				if(litr[j] and can[2*j+1][2*i])
					ok = 1;
			}
			if(ok==0){
				if(bulbs[2*i].S >= bulbs[2*i-2].S){
					litl[i] = 1;
				}
				else{
					litr[i-1] = 1;
				}
			}
		}
		litr[N-1] = 1;
		for(int i=N-2;i>=0;i--){
			int ok = 0;
			//right side of i
			for(int j=i+1;j<N;++j){
				if(can[2*j][2*i+1] and litl[j])
					ok = 1;
			}
			if(ok==0){
				if(bulbs[2*i].S >= bulbs[2*i+2].S){
					litr[i] = 1;
				}
				else{
					litl[i+1] = 1;
				}
			}
		}
		int ans = 0;
		for(int i=0;i<N;++i)ans += litl[i] + litr[i] ;
		//	cout<<i<<' '<<litl[i]<<' '<<litr[i]<<endl;
		cout<<ans<<endl;

	}
	return 0;
}
