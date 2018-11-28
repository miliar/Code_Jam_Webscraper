#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

long long c[40];
long long b[40];

int main(){
    int tt,TT,n,i,j,dc,k,g;
    long long S,s;
    double md,d;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ){
        scanf("%I64d",&S);
        scanf("%d",&n);
        for( i=0; i<n; i++ ){
            scanf("%I64d",&c[i]);
        }
        for( ; i<37; i++ ){
            c[i]=0;
        }
        n=37;
        sort(c,c+n);
        c[n]=1000000000000000000LL;
        k=0;
        s=0;
        md=0;
        for( i=0; i<n; i++ ){
            b[i]=c[i];
        }
        while(s<S){
            k=36;
            for( i=35; i>=0; i-- ){
                if(b[i]<b[k]) k=i;
            }
            b[k]++;
            s++;
            k=1000000;
            for( i=0; i<36; i++ ){
                if(b[i]<k) { k=b[i]; g=1; }
                else if(b[i]==k) g++;
            }
            d=0;
            for( i=0; i<36; i++ ){
                if(b[i]==k){
                    d+=(b[i]-c[i])*36/(double)g;
                }
            }
            d-=s;
            if(d>md) md=d;
        }
        printf("Case #%d: %.12f\n",tt+1,md);
    }
    return 0;
}
