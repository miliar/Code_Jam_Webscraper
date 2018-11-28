#include <cstdio>
#include <iostream>
#include <math.h>

using namespace std;

#define MAXN 1001

int T, D;
int dnr[MAXN];

int main(){

    scanf("%d ", &T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d ", &D);
        for(int i=0;i<MAXN;i++) dnr[i] = 0;
        int max=0;


        for(int i=0; i<D;i++){
            int c;
            scanf("%d ", &c);
            dnr[c]+=1;
            max = c>max?c:max;        
        }

        int mt = max;

        

        //
        for(int et=1;et<=MAXN;et++){
            int tt = 0;
            for(int i=1; i<=max; i++){
                

                int sm = dnr[i] * ((int) ceil((1.0*i) / et) - 1);
                tt += sm;
            }
            tt += et;
            mt = mt < tt? mt:tt;


        }


        printf("Case #%d: %d\n", cas,mt);


    }

    return 0;
}
