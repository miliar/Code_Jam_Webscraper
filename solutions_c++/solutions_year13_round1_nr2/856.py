#include <stdio.h>
#include <stdlib.h>
int T;
int E,R,N,v[10],w[10];

int main(){
    freopen("b1.in","r",stdin);
    freopen("b1.out","w",stdout);
    scanf("%d",&T);
    for (int tt= 1 ; tt <= T ; tt++){
        scanf("%d %d %d",&E,&R,&N);
        for (int i = 0 ; i < N ; i++){
            scanf("%d",&v[i]);
        }
        //printf("E%d R%d N%d\n",E,R,N);
        int e = E;
        int ans = 0;
        for (int i = 0 ; i < N ; i++){
            w[i] = -1;
            for (int j = i+1 ; j < N && w[i] == -1; j++){
                if (v[j] > v[i]) w[i] = j;
            }
            //printf("W[%d] = %d\n",i,w[i]);
            if (w[i] == -1) {
                ans += e*v[i];
                e = 0;
            }
            else {
                int time = w[i] - i;
                int maxe = e+R*time;
                int usee = maxe - E;
                //printf("time%d max%d use%d\n",time,maxe,usee);
                if (usee >= 0) {
                    if (e < usee) usee = e;
                    e -= usee;
                    ans += usee*v[i];
                }
            }
            e+=R;
            if (e > E) e = E;
        }
        
        printf("Case #%d: %d\n",tt,ans);
    }
}
