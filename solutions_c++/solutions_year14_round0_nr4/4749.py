#include <cstdio>
#include <queue>
#include <limits.h>
#include <cstring>
#include <map>
#include <string>
#include <vector>
using namespace std;
#define MAXN 1010
#define INF INT_MAX //nao ha perigo de overflow

int main(){
    int t,n;
    int res1,res2;
    float nao[MAXN],k[MAXN];

    scanf("%d", &t);
    for(int f = 0;f<t;f++){
        //printf("Oi\n");
        scanf("%d", &n);
        for(int a=0;a<n;a++){
            scanf("%f",&nao[a]);
        }
        for(int a = 0;a<n;a++){
            scanf("%f", &k[a]);
        }

        sort(k,k+n);
        sort(nao,nao+n);
        res1 = 0;res2 = 0;
        int j = 0;
        for(int i = 0;i<n;i++){
            if(nao[i]>k[j]){
                res1++;
                j++;
            }
        }
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                if(nao[i] > 0 && k[j] > 0 && k[j]>nao[i]){
                    nao[i] =-1;
                    k[j] = -1;
                    break;
                }
            }
            if(nao[i]>0){
                nao[i]--;
                for(int j=0;j<n;j++){
                    if(k[j]>0){
                        k[j] = -1;
                        break;
                    }
                }
                res2++;
            }

        }
        printf("Case #%d: %d %d\n", f+1,res1,res2);

    }
    return 0;

}