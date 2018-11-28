#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int tests;
int n,k;
int bt[35];
ll _pow(ll base,ll p){
    ll res=1;
    while(p){
        if(p&1){
            res*=base;
        }
        base*=base;
        p>>=1;
    }
    return res;
}
vector<pair<string,vector<ll>>> v;
ll isprime(ll n){
    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0) return i;
    }
    return 0;
}


void calc(){
    vector<ll> vc;
    for(int base=2;base<=10;base++){
        int p=0;
        ll u=0;
        for(int index=n-1;index>=0;index--){
            u+=bt[index]*_pow(base,p++);
        }
        ll k=isprime(u);
        if(k!=0) vc.push_back(k);
    }
    if(vc.size()==9){
        string st="";
        int jk=0;
        while(jk<n){
            st+=char(bt[jk++]+'0');
        }
        v.push_back({st,vc});
    }



}
void rec(int in){
    if(in==n-1) {

        calc();
        return;
    }
    if(v.size()>k) return;
    bt[in]=0;
    rec(in+1);
    bt[in]=1;
    rec(in+1);

}

int main() {
//    freopen(".in","r",stdin);
    freopen("sabbir.txt","w",stdout);
    scanf("%d ",&tests);
    for(int t=1; t<=tests; t++) {
        cin >> n >> k;
        bt[0]=1;
        bt[n-1]=1;
        rec(1);
        printf("Case #%d:\n",t);
        int cnt=0;
        for(auto x:v){
            if(cnt++==k) break;
             cout<<x.first<<" ";
            for(auto cx:x.second){
                cout<<cx<<" ";
            }
            cout<<endl;

        }

    }
}
