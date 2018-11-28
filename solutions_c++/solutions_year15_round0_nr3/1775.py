#include <stdio.h>
#define min(a,b) ( (a) < (b) ? (a) : (b) )
#define L 0
#define NL  4
#define I 1
#define NI 5
#define J 2
#define NJ 6
#define K 3
#define NK 7
int op[8][8] = {
    //1, i, j, k, -1, -i, -j, -k
    { L, I, J, K, NL, NI, NJ, NK},//1
    { I, NL,K,NJ, NI, L,  NK, J},//i
    { J, NK,NL,I, NJ, K,  L,  NI},//j
    { K, J, NI,NL,NK,NJ,  I, L},//k
    { NL,NI,NJ,NK, L, I, J, K},//1
    { NI,L ,NK,J , I,NL, K,NJ},//i
    { NJ,K ,L ,NI, J,NK,NL, I},//j
    { NK,NJ,I ,L , K, J,NI,NL}//k
};
int main(){
    freopen("test.in","r",stdin);
    freopen("small.out","w",stdout);
    int T;
    int tt = 1;
    scanf("%d",&T);
    while(T--){
        int n,k;
        scanf("%d %d\n",&n,&k);
        char s[10005];
        scanf("%s",s);
        int cur = L;
        int state = 0;
        for(int kk = 0; kk < k;kk++){
            for(int i = 0;i < n;i++){
                char c = s[i];
                int dd = c - 'i' + 1;
                cur = op[cur][dd];
                if(state == 0 && cur == I){
                    state = 1;
                }else if(state == 1 && cur == K){
                    state = 2;
                }
            }
        }
        // int part = cur;
        // for(int i = 0;i < min(n,10000);i++){
        //     cur = op[cur][tmp[i]];
        //     if(state == 0 && cur == I){
        //         state = 1;
        //     }else if(state == 1 && cur == K){
        //         state = 2;
        //     }
        // }
        // cur = part;
        // for(int i = 0; i < k - 1;i++){
        //     cur = op[cur][part];
        //     if(state == 0 && cur == I){
        //         state = 1;
        //     }else if(state == 1 && cur == K){
        //         state = 2;
        //     }
        // }
        if(cur == NL && state == 2){
            printf("Case #%d: Yes\n",tt++);
        }else{
            printf("Case #%d: No\n",tt++);
        }
    }

}