
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define N 3030
#define MOD 1000002013

using namespace std;
typedef long long int LL;
typedef pair<LL,LL> PII;

LL n,m,sm;
PII e[N];

LL cost(LL t){
	return ( (n+n-t+1)*t/2 )%MOD;
}

void input(){
	cin >> n >> m;
	LL x,y,p;
	sm = 0;
	int en=0;
	for(int i=0;i<m;i++){
		cin >> x >> y >> p;
		e[en++] = PII(x,p); 
		e[en++] = PII(y,-p);
		sm = (sm + cost(y-x)*p)%MOD;
	}
}

bool cmp(const PII& a, const PII& b){
	if(a.first != b.first) return a.first<b.first;
	return a.second>b.second;
}

void solve(){
	sort(e,e+2*m,cmp);
	LL ans=0;
	PII s[N];
	int sn=0;
	for(int i=0; i<2*m; i++){
		if(e[i].second>0){
			s[sn++] = e[i];
		}
		else{
			LL y = e[i].first, p = -e[i].second;
			while(p){
				LL x = s[sn-1].first, xp = s[sn-1].second;
				if(p>=xp){
					ans = ( ans + cost(y-x)*xp )%MOD;
					p-=xp;
					sn--;
				}
				else{
					ans = ( ans + cost(y-x)*p )%MOD;
					s[sn-1].second -= p;
					p = 0;
				}
			}
		}
	}
	ans = (MOD + sm-ans)%MOD;
	static int xi=0;
	printf("Case #%d: %d\n", ++xi, (int)ans);
}

int main(){
	int zn;
	scanf("%d",&zn);
	while(zn--){
		input();
		solve();
	}
	return 0;
}

