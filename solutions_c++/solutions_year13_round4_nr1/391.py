#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
using namespace std;

template<class T>inline void ChkMax(T &a,const T &b){if(a < b) a = b;}
template<class T>inline void ChkMin(T &a,const T &b){if(b < a) a = b;}
const int dx[]={ 0, 0,-1, 1,-1, 1,-1, 1};
const int dy[]={-1, 1, 0, 0,-1,-1, 1, 1};

typedef long long LL;
typedef pair<int, int> pii;

#define LOWBIT(v) ((v)&(-(v)))
#define POW2(p) (1<<(p))
#define KTH_BIT(v, k) ((v) & POW2(k))
#define MERGE_BIT(v, k) ((v) | POW2(k))
#define INF 0x3f3f3f3f
#define eps 1e-5

// -------------------------------------------

#define MAXN 
#define MAXM 1003
#define MOD 1000002013

int n, m;
int tot;

struct Data {
	int t, p;
	int flag;
	bool operator<(const Data &tmp) const {
		if(t == tmp.t) {
			return flag > tmp.flag;
		}
		return t<tmp.t;
	}
}data[MAXM*2], tmp[2][MAXM];

LL calc(LL dif_t, LL chg) {
	LL a = n+n+1-dif_t;
	LL b = dif_t;
	if(a & 1) {
		b>>=1;
	} else {
		a>>=1;
	}
	LL ret = a*b%MOD;
	ret = ret*chg%MOD;

	return ret;
}

int solve() {
	LL ret = 0;
	for(int i=0; i<tot; ) {
		LL getin = 0;
		int lin = 0;
		int lout = 0;
		int k = i;
		for( ; k<tot; ) {
			getin += data[k].p*data[k].flag;

			if(data[k].flag == 1) {
				tmp[0][lin++] = data[k];
			} else {
				tmp[1][lout++] = data[k];
			}
			++k;
			if(getin <= 0) {
				break;
			}
		}
		
		i = k;

		for(int b=0; b<lout; ++b) {
			for(int a = lin-1; a>=0; --a) {
				if(tmp[0][a].t > tmp[1][b].t) {
					continue;
				}
				LL chg = min(tmp[0][a].p, tmp[1][b].p);
				ret += calc(tmp[1][b].t-tmp[0][a].t, chg);
				ret %= MOD;
				tmp[0][a].p -= chg;
				tmp[1][b].p -= chg;
				if(tmp[1][b].p == 0) {
					break;
				}
			}
		}
				
	}
	return ret % MOD;
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("in", "r", stdin);
	freopen("C:\\Users\\Tang\\Downloads\\A-large.in", "r", stdin);
	freopen("C:\\Users\\Tang\\Downloads\\a.out", "w", stdout);	
#endif
	
	int dataset;
	scanf("%d", &dataset);
	for(int cas=1; cas<=dataset; ++cas) {
		scanf("%d %d", &n, &m);
		int s, e, p;
		LL fee = 0;
		for(int i=0; i<m; ++i) {
			scanf("%d %d %d", &s, &e, &p);
			fee = (fee + calc(e-s, p))%MOD;

			data[i].t = s;
			data[i].p = p;
			data[i].flag = 1;

			data[i+m].t = e;
			data[i+m].p = p;
			data[i+m].flag = -1;
		}
		tot = m*2;
		sort(data, data+tot);
		printf("Case #%d: %d\n", cas, ((fee-solve())%MOD+MOD)%MOD);
	}

	return 0;
}
