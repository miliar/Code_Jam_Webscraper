#include <iostream>
#include <cstring>
#include <queue>
#include <cstdio>
#include <map>
#include <string>
using namespace std;
int n,x[1100];
string s;
int solve(){
    cin>>n>>s;
    for(int i=0;i<=n;i++)x[i]=s[i]-'0';
    int cur=0,ans=0;
    for(int i=0;i<=n;i++)if(x[i]!=0){
        if(cur>=i){
            cur+=x[i];
        }else{
            ans+=i-cur;
            cur=i+x[i];
        }
    }
    return ans;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        printf("Case #%d: %d\n",i,solve());
    }
    return(0);
}
