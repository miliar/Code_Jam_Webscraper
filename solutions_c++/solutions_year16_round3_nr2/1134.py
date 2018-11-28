#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;

int ans[55];
int main(){
    int n,t,i,j,k;
    int in;

    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);

    long long b,m;

    scanf("%d",&t);

    for(k=1;k<=t;k++) {
        scanf("%lld%lld",&b,&m);
        printf("Case #%d: ",k);

       // printf("%lld ",1<<(b-2));
        if(m > (1<<(b-2))) {
            printf("IMPOSSIBLE\n");
            continue;
        } else {
            printf("POSSIBLE\n");
        }

        long long tmp = m;

        for(i=0;i<51;i++)
            ans[i] = 0;

        if(m == (1<<(b-2))) {
            ans[1] = 1;
            tmp--;
        }


        i=2;
        while(tmp > 0) {
            ans[i++] = tmp%2;
            tmp/=2;
        }

        for(i=1;i<=b;i++) {
            for(j=1;j<b;j++) {
                if(j>i) printf("1");
                else printf("0");
            }
            printf("%d\n",ans[i]);

        }

        //printf("\n");
    }
}
