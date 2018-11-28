#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>

using namespace std;

int T,n,ans,now,tmp,A,a[10000];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for (int tt=1;tt<=T;tt++){
        scanf("%d%d",&A,&n);
        for (int i=0;i<n;i++) scanf("%d",&a[i]);sort(a,a+n);
        ans=n;now=0;tmp=0;
        while (true){
              if (tmp>n) break;
              while (now<n&&a[now]<A) A+=a[now],now++;
              if (now>=n) {ans=min(ans,tmp);break;}
              ans=min(ans,tmp+n-now);A+=A-1;tmp++;
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
