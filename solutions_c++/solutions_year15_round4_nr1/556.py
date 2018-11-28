#include<bits/stdc++.h>
#define next sled
const int N=120;
using namespace std;
char a[N][N];
int n,m,q[N],w[N],ans;
int ok;
int t,non;
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    cin>>t;
    for(int tt=1;tt<=t;++tt){
    cout<<"Case #"<<tt<<": ";
    cin>>n>>m;
    ok=0;
    for(int i=1;i<=max(n,m);++i)
        q[i]=w[i]=0;
    non=ans=0;
    for(int i=1;i<=n;++i)
    for(int j=1;j<=m;++j){
        cin>>a[i][j];
        if(a[i][j]!='.'){
            ++non;
            ++q[i];
            ++w[j];
        }
    }
    for(int i=1;i<=n;++i)
    for(int j=1;j<=m;++j){
        if(a[i][j]!='.'){
            if(q[i]+w[j]==2)ok=1;
        }
    }
    if(ok==1){
        cout<<"IMPOSSIBLE\n";
        continue;
    }
    for(int i=1;i<=n;++i)
    for(int j=1;j<=m;++j){
        if(a[i][j]=='<'){
            for(int k=j-1;k>=1;--k)
            if(a[i][k]!='.'){
                ++ans;
                break;
            }
        }
        if(a[i][j]=='>'){
            for(int k=j+1;k<=m;++k)
            if(a[i][k]!='.'){
                ++ans;
                break;
            }
        }
        if(a[i][j]=='^'){
            for(int k=i-1;k>=1;--k)
            if(a[k][j]!='.'){
                ++ans;
                break;
            }
        }
        if(a[i][j]=='v'){
            for(int k=i+1;k<=n;++k)
            if(a[k][j]!='.'){
                ++ans;
                break;
            }
        }
    }
    cout<<non-ans;
    cout<<"\n";
    }

}
