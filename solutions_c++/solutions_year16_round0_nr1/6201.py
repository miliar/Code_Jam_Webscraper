#include <cstdio>
#include <cstdlib>
using namespace std;
const int MAXN = 1000000 + 9;
int ans[MAXN] = {0};

int calc(int x){
    int ret = 0;
    while(x){
        ret |= 1 << (x % 10);
        x /= 10;
    }
    return ret;
}
int main(){
    int lim = (1 << 10) - 1,T;
    scanf("%d",&T);
    for(int Cas = 1;Cas <= T;++ Cas){
        printf("Case #%d: ",Cas);
        int msk = 0,j,i;
        scanf("%d",&i);
        if(i == 0){
            puts("INSOMNIA");
            continue;
        }
        if(ans[i] != 0){
            printf("%d\n",ans[i]);
            continue;
        }
        j = i;
        msk |= calc(j);
        while(msk < lim){
            j += i;
            msk |= calc(j);
        }
        printf("%d\n",ans[i] = j);
    }
    return 0;
}
