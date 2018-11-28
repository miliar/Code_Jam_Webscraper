#include <stdio.h>
#include <algorithm>
using namespace std;

int c[10000];

int main(){
    int TT,n,s;
    scanf("%d",&TT);
    for( int tt=0; tt<TT; tt++ ){
        scanf("%d",&n);
        for( int i=0; i<n; i++ ){
            scanf("%d",&c[i]);
        }
        s = 0;
        for( int i=n; i>0; i-- ){
            int mj = 0;
            for( int j=1; j<i; j++ ){
                if(c[j]<c[mj]) mj = j;
            }
            s += min(mj,i-mj-1);
            for( int j=mj; j<i-1; j++ ){
                c[j] = c[j+1];
            }
        }
        printf("Case #%d: %d\n",tt+1,s);
    }
    return 0;
}
