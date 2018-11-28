#include<bits/stdc++.h>
using namespace std;
string s;
int a[1005];
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,e,f,i,k,m,n,z;
    cin>>t;
    for(k=1;k<=t;++k){
        z=0;
        cin>>s>>m;
        n=s.size();
        for(i=0;i<n;++i) a[i]=0;
        for(i=e=0;i<n;++i){
            if(s[i]=='+') f=0; else f=1;
            e-=a[i];
            if(e%2!=f){
                if(i+m>n) break;
                else{
                    ++z;
                    ++e;
                    ++a[i+m];
                }
            }
        }
        printf("Case #%d: ",k);
        if(i<n) printf("IMPOSSIBLE\n"); else printf("%d\n",z);
    }
}
