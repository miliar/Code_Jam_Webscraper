#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int a[5][5], b[5][5];
int ca[17], cb[17], c[17];
int na, nb, n;
int main(){     freopen("A-small-attempt1.in", "r", stdin);
                freopen("A-small-attempt1.out","w", stdout);
    int T, now;
    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        memset(c, 0, sizeof(c));
        scanf("%d", &n);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++){
                scanf("%d", &now);
                if( i==n ){
                    c[now]++;
                }
            }
        scanf("%d", &n);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++){
                scanf("%d", &now);
                if( i==n ){
                    c[now]++;
                }
            }
        int counter=0, Nans=0, ans;
        for(int i=1; i<=16; i++){
            if( c[i] ){
                counter++;
                if( 2==c[i] ){
                    Nans++;
                    ans = i;
                }
            }
        }
        if( 7==counter )     printf("Case #%d: %d\n", t, ans);
        else if( Nans>1 )    printf("Case #%d: Bad magician!\n", t);
        else                 printf("Case #%d: Volunteer cheated!\n", t);
    }
    return 0;
}
