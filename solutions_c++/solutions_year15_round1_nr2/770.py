#include<bits/stdc++.h>
using namespace std;

void solve(){
    long long b,n;
    cin >> b >> n;
    vector<long long>v(b);
    for(int i = 0 ; i < b ; ++ i ){
        cin >> v[i];
    }
    long long s = 0 , e =100000LL*1e9;

    while(s<=e){
        long long m =(s+e)/2;
        long long p = 0;
        long long c0=0;
        for(int i = 0 ; i < b ; ++ i ){
            p+= (m+v[i])/v[i];
            if(m%v[i]==0)c0++;
        }
        if(p>=n&&p-c0<n){
            long long toFind =n-(p-c0);
            for(int i = 0 ; i < b ; ++ i ){
                if(m%v[i]==0){
                    toFind--;
                    if(toFind==0){
                        printf("%d\n",i+1);
                        return ;
                    }
                }
            }
        }
        else if(p>=n){
            e=m-1;
        }
        else s=m+1;
    }
}

int main(){
    freopen("B-large"".in","r",stdin);
    freopen("B-large"".out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;

}
