#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    long long fact[21];
    fact[0]=1;
    for(long long i=1;i<21;i++){
        fact[i]=fact[i-1]*i;
    }
    for(int z=1;z<=t;z++){
        long long b,m;
        cin>>b>>m;
        if((1LL<<(b-2)<m)){
            cout<<"Case #"<<z<<": IMPOSSIBLE\n";
            continue;
        }
        cout<<"Case #"<<z<<": POSSIBLE\n";
        long long x[b+1];
        x[b]=1;
        for(int i=b-1;i>=1;i--){
            x[i]=1LL<<(i-(b-1));
        }
        string s[b];
        for(int i=0;i<b;i++){
            for(int j=0;j<b;j++){
                if(i==0)s[i]+='0';
                else if(j<=i)s[i]+='0';
                else s[i]+='1';
            }
        }
        if(m==((1LL<<(b-2)))){
            for(int i=1;i<b;i++)s[0][i]='1';
        }else{
            for(long long i=0;i<b;i++){
                if(m&(1LL<<i)){
                    s[0][b-i-2]='1';
                }
            }
        }
        for(int i=0;i<b;i++)cout<<s[i]<<"\n";
    }
    return 0;
}
