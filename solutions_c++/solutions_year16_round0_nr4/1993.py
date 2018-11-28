#include <cstdio>
#include <algorithm>

using namespace std;

long long gq( int a, int k, int c ) {
    long long r=0;
    while ( c-- ) {
        r=r*k+(a++);
    }
    return r+1;
}

int main() {
    int t,eeeeee;
    scanf("%d",&t);
    eeeeee=t;
    while ( t-- ) {
        int k,c,s;
        scanf("%d%d%d",&k,&c,&s);
        long long W[100];
        int ilw = 0;
        int aa;
        for ( aa=0; aa+c<=k; aa+=c ) W[ilw++]=gq( aa, k, c );
        if ( aa<k ) W[ilw++] = gq( aa, k, k-aa );
        if ( ilw>s ) printf("Case #%d: IMPOSSIBLE\n",eeeeee-t);
            else {
                printf("Case #%d: ",eeeeee-t);
                for ( int i=0; i<ilw; i++ ) printf("%lld ",W[i]);
                printf("\n");
            }
    }
    return 0;
}

