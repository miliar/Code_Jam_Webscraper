#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;

#define fr(a,b,c) for(int a=b;a<c;a++)
#define rp(a,b) fr(a,0,b)
#define cl(a,b) memset(a,b,sizeof(a))

int v[10];

int main(){
    int t; scanf("%d",&t); t++;
    cl(v,0);
    fr(cas,1,t){
        printf("Case #%d: ",cas);
        int row; 
        scanf("%d",&row);
        for(int i=1;i<=4;i++){
            if(i==row) rp(j,4) scanf("%d",&v[j]);
            else rp(j,4) scanf("%*d");
        }
        sort(v,v+4);
        scanf("%d",&row);
        int cont=0,ans=0;
        for(int i=1;i<=4;i++){
            if(i==row){
                int aux;
                rp(j,4){
                     scanf("%d",&aux);
                     int k=lower_bound(v,v+4,aux)-v;
                     if(v[k]==aux){
                        ans=aux;
                        cont++;
                     }
                }
            }else rp(j,4) scanf("%*d");
        }
        if(cont==1) printf("%d\n",ans);
        else if(cont > 1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}

