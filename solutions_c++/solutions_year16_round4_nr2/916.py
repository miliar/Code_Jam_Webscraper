#include<bits/stdc++.h>
using namespace std;
int main(){
//    ios_base::sync_with_stdio(0);
//    cin.tie(nullptr);
    freopen("in3","r",stdin);
    freopen("out3","w",stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        int n,k;
        cin>>n>>k;
        double p[n];
        for(int i=0;i<n;i++){
            cin>>p[i];
        }
        double mx=0;
        for(int i=0;i<(1<<n);i++){
            if(__builtin_popcount(i)==k){
                double sum=0.0;
                vector<int>v;
                for(int j=0;j<n;j++){
                    if(i&(1<<j)){
                        v.push_back(j);
                    }
                }
                for(int j=0;j<(1<<k);j++){
                    if(__builtin_popcount(j)==(k/2)){
                        double x=1.0;
                        for(int l=0;l<k;l++){
                            if(j&(1<<l))x*=p[v[l]];
                            else x*=(1.0-p[v[l]]);
                        }
                        sum+=x;
                    }
                }
                mx=max(mx,sum);
            }
        }
        cout<<"Case #"<<z<<": "<<fixed<<setprecision(8)<<mx<<"\n";
    }
    return 0;
}
