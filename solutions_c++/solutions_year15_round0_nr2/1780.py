#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define maxn 1010
#define inf 2000000000
using namespace std;
int T,maxd,ans,cnt,n;
int a[maxn];
int Get(int x,int y){
    int d=x/y;
    if(x%y==0) d--;
    return d;
}
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d",&n);
        maxd=0;
        ans=inf;
        for(int i=0;i<n;i++) scanf("%d",&a[i]),maxd=max(maxd,a[i]);
        //printf("%d\n",maxd);
        for(int i=1;i<=maxd;i++){
            cnt=i;
            for(int j=0;j<n;j++) cnt+=Get(a[j],i);
            ans=min(ans,cnt);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
