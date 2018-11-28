#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<unordered_map>
using namespace std;
 int bff[10000];
    int stav[10000];
    int flag[10000];
    int maxdelka[10000];
int main(void){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int l; int T;
    scanf("%i",&T);
    for(l=0;l<T;l++){
        printf("Case #%i: ", l+1);
        int N;
        int i;
        scanf("%i", &N);
        for(i=0;i<N;i++){
            scanf("%i", &bff[i]);
            bff[i]--;
            stav[i]=-1;
            flag[i]=0;
            maxdelka[i]=0;
        }
        int j;
        int pocetdvou=0;
        int pridej=0;
        int maxcyklus=0;
        int c;
        int hodne=100000;
        for(i=0;i<N;i++){
            if(i==bff[bff[i]]) stav[i]=hodne;
        }
        for(i=0;i<N;i++){
            if(stav[i]<=i){
                c=i;
                for(j=0;;j++){
                    if(stav[c]<i) {stav[c]=i;flag[c]=j;}
                    else if(stav[c]==i){
                        if(j-flag[c]>maxcyklus) maxcyklus=j-flag[c];
                        break;
                    }
                    else if(stav[c]==hodne){
                        if(j>maxdelka[c]) maxdelka[c]=j;
                        break;
                    }
                    c=bff[c];
                }
            }
        }
        int res=0;
        /*for(i=0;i<10;i++){
            printf("%i ", maxdelka[i]);
        }
        printf("\n");*/
        for(i=0;i<N;i++){
            if(stav[i]==hodne){
                res++; res+=maxdelka[i];
            }
        }
        //printf("%i %i\n", maxcyklus, res);
        if(maxcyklus>=res){
            printf("%i\n", maxcyklus);
        }
        else{
            printf("%i\n", res);
        }
    }
    return 0;
}
