#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

#define MAX 22
#define MAXK 210

using namespace std;

int n,keys,aux,teste;
int mapa[MAXK];
int t[MAX],k[MAX];
vector<int> win[MAX];
vector<int> vet;
int pot[MAX];
int pd[1<<MAX];
//int vezes=0;

int bckt(int mask){

    if(pd[mask]) return 0;
    pd[mask]=1;


   // vezes++;

    //if(vezes> 10000000) printf("mask:%d\n",mask);

    if( __builtin_popcount(mask) == n) return 1;

    for(int i=0;i<n;i++){
        if(mask&pot[i]) continue;
        if(mapa[t[i]] >= 1){
            mapa[t[i]]--;
            for(int j=0;j<k[i];j++){
                mapa[win[i][j]]++;
            }
            int resp=bckt(mask|pot[i]);

            if(resp == 1){
                vet.push_back(i);
                return resp;
            }

            mapa[t[i]]++;
            for(int j=0;j<k[i];j++){
                mapa[win[i][j]]--;
            }

        }
    }

    return 0;

}

int main(void){

    freopen("D.in","r",stdin);

    freopen("D.out","w",stdout);

    for(int i=0;i<MAX;i++){
        pot[i]=1<<i;
    }

    scanf("%d",&teste);

    for(int caso=1;caso<=teste;caso++){
//        vezes=0;

        memset(pd,0,sizeof(pd));

        memset(mapa,0,sizeof(mapa));
        //mapa.clear();
        scanf("%d %d",&keys,&n);

        for(int i=0;i<keys;i++){
            scanf("%d",&aux);
            mapa[aux]++;
        }

        for(int i=0;i<n;i++){
            win[i].clear();
            scanf("%d %d",&t[i],&k[i]);

            for(int j=0;j<k[i];j++){
                scanf("%d",&aux);
                win[i].push_back(aux);
            }
        }
        vet.clear();

        printf("Case #%d:",caso);
        int resp=bckt(0);
        if(!resp) printf(" IMPOSSIBLE\n");
        else{
            reverse(vet.begin(),vet.end());
            for(int i=0;i<vet.size();i++){
                printf(" %d",vet[i]+1);
            }
            printf("\n");
        }

    }
    return 0;
}
