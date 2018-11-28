#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int n,m,T,r1[110],c1[110],r2[110],c2[110],a[110][110];
bool ok;

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
        scanf("%d%d",&n,&m);
        ok=true;
        for (int i=1;i<=n;i++) r1[i]=100;
        for (int i=1;i<=m;i++) c1[i]=100;
        memset(r2,0,sizeof(r2));memset(c2,0,sizeof(c2));
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++){
                scanf("%d",&a[i][j]);
                r1[i]=min(r1[i],a[i][j]);r2[i]=max(r2[i],a[i][j]);
                c1[j]=min(c1[j],a[i][j]);c2[j]=max(c2[j],a[i][j]);
            }
        for (int i=1;i<=n;i++){
            for (int j=1;j<=m;j++){
                if (a[i][j]==r1[i] && a[i][j]!=r2[i] && a[i][j]!=c2[j]) {ok=false;break;}
                if (a[i][j]==c1[j] && a[i][j]!=c2[j] && a[i][j]!=r2[i]) {ok=false;break;}
            }
            if (!ok) break;
        }
        if (ok) printf("Case #%d: YES\n",t); else printf("Case #%d: NO\n",t);
    }
    return 0;
}
