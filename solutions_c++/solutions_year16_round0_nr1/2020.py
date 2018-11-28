#include <cstdio>

using namespace std;

int main() {
    int t,eeeeee;
    scanf("%d",&t);
    eeeeee=t;
    while ( t-- ) {
        int n;
        char c[100];
        int aa=10,i;
        for (i=0; i<10; i++) c[i]=0;
        scanf("%d",&n);
        for ( i=n; i<1000*n; i+=n ) {
            int a = i;
            while ( a ) {int bb = a%10; if (!c[bb]) {aa--; c[bb]=1;} a/=10;}
            if (!aa) break;
        }
        if ( i == 1000*n ) printf("Case #%d: INSOMNIA\n",eeeeee-t);
                     else  printf("Case #%d: %d\n",eeeeee-t,i);
    }
    return 0;
}

