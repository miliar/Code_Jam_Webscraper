/** CyCraig - Google Code Jam 2015 Qualification Problem B **/
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std ;

int diners[1010];

int main(void) {
    freopen("B-large.in","r",stdin);
    freopen("LARGEOUT.out","w",stdout);
    
    int n,d,maxp,minp,sum;
    int cases = 0;
    scanf("%d\n", &n) ;
    while( n-- ) {
        
        scanf("%d", &d) ;
        //printf("d=%d\n",d);
        for(int i = 0 ; i < d ; i++) {
            scanf("%d",&diners[i]);
            maxp = max(diners[i],maxp);
        }
        
        //for(int i = 0; i < d; i++) {
        //    printf("%d ",diners[i]);
        //}
        //printf("\n");
        
        minp = maxp ;
        for(int i = 1 ; i <= maxp ; i++) {
            sum = i ;
            for(int j = 0 ; j < d ; j++) {
                if(diners[j] > i) {
                    if(diners[j]%i==0) sum += ((diners[j]/i)-1);
                    else sum += (diners[j]/i);
                }
            }
            //printf("%d,",sum);
            minp = min(minp,sum);
        }
        //printf("\n");
        printf("Case #%d: %d\n", ++cases, minp);
        //cout << "Case #" << ++cases << ": " << ceil(log2(maxp))+1 << "\n";
    }
    
    return 0;
}
