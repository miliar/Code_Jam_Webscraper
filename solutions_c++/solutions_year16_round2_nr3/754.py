#include<bits/stdc++.h>
using namespace std;
string first[17],last[17];
int n,dp[1<<16];
int rec(int mask){
    if(__builtin_popcount(mask)==n)return 0;
    if(dp[mask]!=-1)return dp[mask];
    int ret=0;
    for(int i=0;i<n;i++){
        if(!(mask&(1<<i))){
            bool ff=0,fl=0;
            for(int j=0;j<n;j++){
                if(mask&(1<<j)){
                    if(first[i]==first[j])ff=1;
                    if(last[i]==last[j])fl=1;
                }
            }
            if(ff&&fl)ret=max(ret,1+rec(mask|(1<<i)));
            else ret=max(ret,rec(mask|(1<<i)));
        }
    }
    return dp[mask]=ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>first[i]>>last[i];
        }
        memset(dp,-1,sizeof(dp));
        cout<<"Case #"<<z<<": "<<rec(0)<<"\n";
    }
    return 0;
}
