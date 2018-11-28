#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <complex>
#include <iostream>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define pb push_back
#define mp make_pair
#define MOD 1000002013LL
using namespace std;

struct move{
    long long o,e,p;
    bool operator<(const move &np) const{
        if(o<np.o) return true;
        if(o>np.o) return false;
        return e<np.e;
    }
};

long long cost(long long d){
    d--;
    long long ret = ((d*d+d)/2)%MOD;
    return ret;
}

long long solve(){
    int n,m;
    scanf("%d%d",&n,&m);
    move z[1000];
    rep(i,m) cin >> z[i].o >> z[i].e >> z[i].p;
    sort(z,z+m);

    long long us = 0;
    rep(i,m) {
        us += z[i].p * cost(z[i].e-z[i].o);
        us %= MOD;
    }


    long long il = 0;
    vector<int> temp,X;
    rep(i,m){temp.pb(z[i].o); temp.pb(z[i].e);}
    sort(temp.begin(),temp.end());
    temp.pb(0);

    rep(i,temp.size()-1){
        if(temp[i] != temp[i+1]) X.pb(temp[i]);
    }

    long long per[2222];
    memset(per,0,sizeof(per));
    rep(i,m){
        rep(j,X.size()-1){
            if(z[i].o <= X[j] && X[j+1] <= z[i].e){
                per[j] += z[i].p;
            }
        }
    }

    int xx = X.size()-1;

    for(int i = 0; i < xx; i++){
        while(per[i] != 0){
            int j;
            long long moving = per[i];
            for(j = i+1; per[j] != 0; j++){
                moving = min(moving,per[j]);
            }
            for(int k = i; k < j; k++){
                per[k] -= moving;
            }
            il += moving * cost(X[j] - X[i]);
            il %= MOD;
        }
    }

    long long ans = (il - us + MOD*9)%MOD;
    return ans;
}



int main(){
    cost(0);
    cost(1);
    cost(2);
    cost(3);
    cost(4);
    int T;
    scanf("%d",&T);
    rep(i,T){
        printf("Case #%d: %lld\n",i+1,solve());
    }
    return 0;
}


