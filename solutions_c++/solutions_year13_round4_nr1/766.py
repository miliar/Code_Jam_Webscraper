#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<assert.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

//#define DEBUG_MODE

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

#ifdef DEBUG_MODE
#define DBG(X) X
#else
#define DBG(X)
#endif

inline int ___INT(){int ret; scanf("%d",&ret); return ret;}
#define INT ___INT()

typedef long long LL;
typedef pair<int,int> pii;

typedef pair<int,LL> pIL;

int N, M;

const LL mod = 1000002013;
const LL modInv = 500001007;

LL fromMap(map<int,LL>& MAP, int key){
    map<int,LL>::iterator it = MAP.find(key);
    if(it!=MAP.end()) return it->second;
    return 0;
}

LL SUM(LL x){
    LL ret = (x * (x + 1))%mod;

    ret = (ret * modInv)%mod;

    return ret;
}

LL getCost(int from, int to){
    int X = to - from;

    return ( SUM(N) - SUM(N-X) + mod)%mod;
}

int main(){

    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);

    int T=INT;

    REP(t,1,T){
        N=INT; M=INT;

        map<int,LL> on, off;
        set<int> stations;

        LL cost = 0;

        FOR(i,M){
            int u = INT;
            int v = INT;
            LL p = INT;

            cost = (cost + (p * getCost(u,v))%mod) %mod;

            on[u] += p; off[v] += p;

            stations.insert(u); stations.insert(v);
        }

        priority_queue<pIL> train;

        for(set<int>::iterator it = stations.begin(); it!=stations.end(); ++it){
            int st = *it;

            LL tmp = fromMap(on,st);

            if(tmp > 0)
                train.push( pIL(st, tmp) );

            LL leaving = fromMap(off,st);

            while (leaving > 0) {
                pIL latest = train.top(); train.pop();

                if(latest.second <= leaving) {
                    leaving -= latest.second;
                    cost = (cost - (latest.second * getCost(latest.first, st))%mod + mod)%mod;
                }else{
                    train.push(pIL(latest.first,latest.second-leaving));
                    cost = (cost - (leaving * getCost(latest.first, st))%mod + mod)%mod;

                    leaving = 0;
                }
            }
        }

        printf("Case #%d: ",t); cout<<cost<<"\n";

    }

    return 0;
}
