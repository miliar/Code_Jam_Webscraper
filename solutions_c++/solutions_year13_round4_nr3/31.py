#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<math.h>
#include<algorithm>
#define ll long long
using namespace std;
int a[2010],b[2010];
int x[2010];
int n;
bool test(int k){
    int L=1,R=1;
    for(int i=0;i<k;i++){
        if(x[i]!=-1&&x[i]<x[k]){
            L=max(L,a[i]+1);
        }
    }
    for(int i=k+1;i<n;i++){
        if(x[i]!=-1&&x[i]<x[k]){
            R=max(R,b[i]+1);
        }
    }
    if(L!=a[k]||R!=b[k])return false;
    for(int i=k+1;i<n;i++){
        if(x[i]==-1){
            if(a[i]<=L)return false;
        }
    }
    for(int i=0;i<k;i++){
        if(x[i]==-1){
            if(b[i]<=R)return false;
        }
    }
    return true;
}
bool dfs(int now){
    //printf("%d\n",now);
    if(now==n){
        for(int i=0;i<n;i++)printf("%d%c",x[i]+1,i+1==n?'\n':' ');
        return true;
    }
    for(int i=0;i<n;i++){
        if(x[i]==-1){
            x[i]=now;
            if(test(i)){
                if(dfs(now+1))return true;
            }
            x[i]=-1;
        }
    }
    return false;
}
void solve(){
    scanf("%d",&n);
    for(int i=0;i<n;i++)x[i]=-1;
    for(int i=0;i<n;i++)scanf("%d",&a[i]);
    for(int i=0;i<n;i++)scanf("%d",&b[i]);
    dfs(0);
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
        //printf("__________________________________\n");
    }
}
