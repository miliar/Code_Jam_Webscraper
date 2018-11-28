#include <stdio.h>
#include <algorithm>
using namespace std;

int c[1000000];

int main(){
    int TT,m,d,n;
    scanf("%d",&TT);
    for( int tt=0; tt<TT; tt++ ){
        scanf("%d %d",&n,&m);
        for( int i=0; i<n; i++ ){
            scanf("%d",&c[i]);
        }
        sort(c,c+n);
        d = n;
        for( int i=0,j=n-1; ; i++ ){
            while(i<j){
                if(c[i]+c[j]<=m){
                    d--;
                    j--;
                    break;
                }
                j--;
            }
            if(i>=j) break;
        }
        printf("Case #%d: %d\n",tt+1,d);
    }
    return 0;
}
