#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
typedef long long ll;
using namespace std;
int main(){
    int t,T,i,j,n,m;
    int a[10];
    bool vis[2000],ok[2000];
    freopen("C-small-attempt0.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d",&T);
    int cou=0;
    bool flag;
    for(i=1;i<=1000;i++){
        j=i;
        cou=0;
        while(j){
            a[cou++]=j%10;
            j/=10;
        }
        flag=1;
        for(j=0;j<cou;j++){
            if(a[j]!=a[cou-j-1]){
                flag=0;
                break;
            }
        }
        vis[i]=flag;
    }
    memset(ok,0,sizeof(ok));
    for(i=1;i*i<=1000;i++){
        if(vis[i] && vis[i*i])
            ok[i*i]=1;
    }
    int ans;
    for(t=1;t<=T;t++){
        scanf("%d %d",&n,&m);
        ans=0;
        for(i=n;i<=m;i++) ans+=ok[i];
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
