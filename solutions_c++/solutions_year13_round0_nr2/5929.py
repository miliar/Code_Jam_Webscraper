#include<cstdio>
#include<algorithm>
#define N 101
using namespace std;

int t,n,m,tab[N][N],pion[N],poziom[N];

int main(){
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++) pion[i]=0;
        for(int j=1;j<=m;j++) poziom[j]=0;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                scanf("%d",&tab[i][j]);
                pion[i]=max(pion[i],tab[i][j]);
                poziom[j]=max(poziom[j],tab[i][j]);
            }
        }
        bool czy=1;
        for(int i=1;i<=n;i++) for(int j=1;j<=m;j++) if(tab[i][j]<min(pion[i],poziom[j])) czy=0;
        if(czy==0) printf("Case #%d: NO\n",test);
        else printf("Case #%d: YES\n",test);
    }
    return 0;
}
