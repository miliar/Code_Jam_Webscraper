#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>
#include<cmath>
using namespace std;

#define LL long long int 
#define PII pair<int,int> 
#define PB push_back
#define MP make_pair
#define INF 1000000000
#define MOD 1000002013
set<pair<LL,LL> > st;
priority_queue<pair<LL,LL> > pq;
map<LL,LL> curtrain;
map<LL,LL> getin;
LL f(LL x, LL n){
    return ((x*(2*n - x + 1))/2)%MOD;
}
LL getf(vector<pair<pair<LL,LL>,LL> > v,LL n){
    LL ret = 0;
    LL i;
    for(i=0;i<v.size();i++){
        ret += (v[i].second*f(v[i].first.second-v[i].first.first,n))%MOD;
        ret %= MOD;
    }
    return ret;
}
vector<pair<pair<LL,LL>,LL> > v;
int main(){
    LL t,i,j,n,m,o,e,p;
    scanf("%Ld",&t);
    LL ts = 0;
    while(t--){
        scanf("%Ld %Ld",&n,&m);
        v.clear();
        vector<pair<pair<LL,LL>,LL> > v2;
        v2.clear();
        getin.clear();
        curtrain.clear();
        while(m--){
            scanf("%Ld %Ld %Ld",&o,&e,&p);
            getin[o] += p;
            getin[e] -= p;
            v.PB(MP(MP(o,e),p));
        }
        LL before = getf(v,n);
        //cout<<before<<endl;
        map<LL,LL> ::iterator it;
        map<LL,LL> ::iterator it2;
        map<LL,LL> ::iterator it3;
        LL left = 0;
        for(it = getin.begin();it != getin.end();it ++){
            if(it->second == 0)continue;
            if(it->second < 0){
                it2 = curtrain.end();
                LL left2 = -it->second;
                for(;it2 != curtrain.begin();){
                    it2 --;
                    if(it2->first <= it->first){
                        LL tmp = min(it2->second,left2);
                        v2.PB(MP(MP(it2->first,it->first),tmp));
                        it2->second -= tmp;
                        left2 -= tmp;
                        if(left2 <= 0){
                            break;
                        }
                    }
                }
            }
            else{
                curtrain[it->first] += it->second;
            }
        }
        cout<<"Case #"<<++ts<<": "<<(-getf(v2,n)+before + MOD)%MOD<<endl;
    }
    return 0;
}

