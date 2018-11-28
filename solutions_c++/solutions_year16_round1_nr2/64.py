#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<unordered_map>
using namespace std;
int main(void){
    freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int l; int T;
    scanf("%i",&T);
    for(l=0;l<T;l++){
        printf("Case #%i:", l+1);
        int h[2507];
        int i;
        int H=2507;
        for(i=0;i<H;i++){
            h[i]=0;
        }
        int N;
        int j;
        int a;
        scanf("%i", &N);
        for(i=0;i<2*N-1;i++){
            for(j=0;j<N;j++){
                scanf("%i", &a);
                h[a]++;
            }
        }
        for(i=0;i<H;i++){
            if(h[i]%2==1) printf(" %i", i);
        }
        printf("\n");

    }
    return 0;
}
