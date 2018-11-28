#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <utility>
#include <map>

#define REP(a,b) for (int a=0; a<b; a++)
#define FOR(a,b,c) for (int a=b; a<=c; a++)
#define FORD(a,b,c) for (int a=b; a>=c; a--)
#define RESET(a,b) memset(a, b, sizeof a)

#define INF 1023123123
#define LL long long
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define PII pair<int,int> 
#define PDD pair<double,double>

#define __ puts("")
#define MAXN 2002
using namespace std;

LL ar[2002];
map<int,int> peta;
int n,nkasus,m;
int a[MAXN],b[MAXN],c[MAXN];
LL w[MAXN];
LL sum;
LL MOD = 1000002013;

LL cost(LL a, LL b){
	LL x = b-a;
	return (x*(x-1)/2) % MOD;
}

int main(){
	scanf("%d", &nkasus);
	REP(jt,nkasus){
		scanf("%d%d", &n, &m);
		peta.clear();
		sum = 0;
		REP(i,m){
			scanf("%d%d%d", &a[i], &b[i], &c[i]);
			peta[a[i]] = 1;
			peta[b[i]] = 1;
			
			sum += (cost(a[i],b[i])*c[i]) % MOD;
			sum %= MOD;
		}
		
		int p = 0;
		for (map<int,int>::iterator it = peta.begin(); it != peta.end(); it++){
			it->S = p;
			w[p] = it->F;
			p++;
		}
		
		RESET(ar, 0);
		REP(i,m){
			a[i] = peta[a[i]];
			b[i] = peta[b[i]];
			ar[a[i]] += c[i];
			ar[b[i]] -= c[i];
		}
		
		vector<LL> uni;
		
		LL cum = 0;
		REP(i,p){
			cum += ar[i];
			ar[i] = cum;
			
			uni.PB(cum);
		}
		
		sort(uni.begin(), uni.end());
		uni.erase(unique(uni.begin(), uni.end()), uni.end());
		
		
		LL minu = 0;
		REP(i,uni.size()){
//			printf(": %lld\n", uni[i]);
			LL dah = 0;
			LL jum = uni[i] - ((i == 0) ? 0 : uni[i-1]);
			REP(j,p){
				if (ar[j] < uni[i]){
					//evaluate
//					printf("%lld %lld = %lld\n", dah, jum, (cost(0,dah) * jum) % MOD);
					minu += (cost(0,dah) * jum) % MOD;
					minu %= MOD;
					dah = 0;
				}else{
					dah += w[j+1] - w[j];
				}
			}
		}
		
		printf("Case #%d: %lld\n", jt+1,((minu - sum)%MOD + MOD) % MOD);
	}
	return 0;
}
