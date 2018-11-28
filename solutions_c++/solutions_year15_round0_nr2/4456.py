#include <cstdio>
#include <algorithm>
using std::min;

const int Limit = 9;
int P[2000];
int Tmp[2000];

int main(){
    int T;
    scanf("%d", &T);
    for(int caset=1 ; caset<=T ; caset++){
        int D;
        scanf("%d", &D);
        for(int i=0 ; i<=Limit ; i++) P[i] = 0;
        for(int i=0 ; i<D ; i++){
            int Pi;
            scanf("%d", &Pi);
            P[Pi]++;
        }
        int res = 0;
        for(int i=0 ; i<=Limit ; i++){
            if(P[i]) res = i;
            Tmp[i] = P[i];
        }
        int TmpRes;
        if(P[9]){
            TmpRes = Tmp[9];
            Tmp[3] += Tmp[9];
            Tmp[6] += Tmp[9];
            for(int i=8;i>2;i--){
                int max =0 ;
                for(int j=1;j<=i;j++){
                    if(j) max = j;
                }
                res = min(res, TmpRes+max);
                TmpRes += Tmp[i];
                Tmp[i/2] += Tmp[i];
                Tmp[(i+1)/2] += Tmp[i];
            }
        }
        TmpRes = P[9]; 
        P[4] += P[9];
        P[5] += P[9];P[9] = 0;
        for(int i=8;i>1;i--){
            int max =0 ;
            for(int j=1;j<=i;j++){
                if(j) max = j;
            }
            res = min(res, TmpRes+max);
            TmpRes += P[i];
            P[i/2] += P[i];
            P[(i+1)/2] += P[i];
            P[i] = 0;
        }
        printf("Case #%d: %d\n", caset, res);
    }
    return 0;
}