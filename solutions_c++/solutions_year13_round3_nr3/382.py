#include <stdio.h>
#include <stdlib.h>

int T,N;
int d,n,w,e,s,dd,dp,ds;

struct even{
    int d,w,e,s;
};
int n_ev;
even ev[1000000];

int compare(const void *a , const void *b) {
    return ((even*)a)->w - ((even*)b)->w;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for (int ttt = 1 ; ttt <= T ; ttt++) {
        scanf("%d",&N);
        n_ev = 0;
        for (int i = 0 ; i < N ; i++){
            scanf("%d %d %d %d %d %d %d %d",&d,&n,&w,&e,&s,&dd,&dp,&ds);
            int td = d;
            int tw = w;
            int te = e;
            int ts = s;
            for (int j = 0 ; j < n;j++) {
                ev[n_ev].d = td;
                ev[n_ev].w = tw;
                ev[n_ev].e = te;
                ev[n_ev].s = ts;
                n_ev++;
                td += dd;
                tw += dp;
                te += dp;
                ts += ds;
            }
        }
         qsort (ev, n_ev, sizeof(ev[0]), compare);
        int ans = 0;
        for (int i = 0; i < n_ev; i++){
            d = ev[i].d;
            w = ev[i].w;
            e = ev[i].e;
            s = ev[i].s;
           // printf("{%d,%d,%d,%d}",d,w,e,s);
            for (int j = 0 ; j < n_ev && ev[j].w <= w  ; j++){
                if (ev[j].d < d && ev[j].s >= s && ev[j].e > w) {
                    w = ev[j].e;
                    
                    //printf("[%d(%d)]",j,w);
                }
            }
            if (w < e) {
                ans++;
                //printf(" 1\n");
            }  //else printf("\n");
        }
        printf("Case #%d: %d\n",ttt,ans);
    } 
}
