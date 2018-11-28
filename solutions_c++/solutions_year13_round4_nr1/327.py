#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<set>
using namespace std;

typedef long long LL;

const LL MOD=1000002013LL;

int N, M, O[1024], E[1024], P[1024];
LL dd[10000];
int len[10000];

LL cost(LL k) {
    if (k%2==1) return (k*N%MOD - (k-1)/2*k%MOD) % MOD;
    return (k*N%MOD - k/2*(k-1)%MOD) % MOD;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int tc=1; tc<=T; tc++) {
	scanf("%d%d", &N, &M);
	for (int i=0; i<M; i++) scanf("%d%d%d", O+i, E+i, P+i);

	vector<int>in(M), out(M), v;
	set<int>se;
	int L;
	for (int i=0; i<M; i++) {
	    se.insert(O[i]-1);	    
	    se.insert(O[i]);
	    se.insert(E[i]-1);
	    se.insert(E[i]);
	}
	v=vector<int>(se.begin(), se.end());
	L=v.size();
	for (int i=0; i<M; i++) {
	    int k;
	    k=lower_bound(v.begin(), v.end(), O[i])-v.begin();
	    in[i]=k;
	    k=lower_bound(v.begin(), v.end(), E[i])-v.begin();
	    out[i]=k;
	}
	se.clear();
	
	LL sum=0, mon=0;
	for (int i=0; i<M; i++) sum = (sum + P[i]*cost(E[i]-O[i])) % MOD;

	memset(dd, 0, sizeof dd);

	for (int i=0; i<M; i++) {
	    dd[in[i]] += P[i];	    
	    dd[out[i]] -= P[i];
	}
	for (int i=0; i<=L; i++) dd[i+1] += dd[i];
	
	//for (int i=0; i<L; i++) printf("(%d %d), ", int(v[i]), int(dd[i])); puts("");
	for (;;) {
	    memset(len, 0, sizeof len);
	    if (dd[0]) len[0]=1;
	    for (int i=1; i<L; i++) if (dd[i]) len[i]=len[i-1]+1;
	    int k=0;
	    for (int i=0; i<L; i++) if (len[k]<len[i]) k=i;
	    if (len[k]==0) break;
	    LL mi=dd[k];
	    for (int i=0; i<len[k]; i++) {
		mi=min(mi, dd[k-i]);
	    }

	    mon = (mon + mi%MOD * cost(v[k]-v[k-len[k]+1]+1)) % MOD;
	    for (int i=0; i<len[k]; i++) dd[k-i]-=mi;
	}
	

	printf("Case #%d: %lld\n", tc, ((sum-mon)%MOD+MOD)%MOD);
	//printf("%lld %lld\n", sum, mon);
    }
    
    return 0;
}
