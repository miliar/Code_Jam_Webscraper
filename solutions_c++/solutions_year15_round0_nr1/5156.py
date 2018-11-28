#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std ;

char a[1111] ;
int main() {
    int t ;
    freopen("A-large.in","r",stdin) ;
    freopen("A-large.out","w",stdout) ;
    cin >> t ;int ca = 0 ;
    while(t -- ) {
        int x ;
        cin >> x ;
        scanf("%s",a) ;
        int l = strlen(a) ;
        int ans = 0 ;
        int sum = 0 ;
        sum = a[0] - '0' ;
        for (int i = 1 ; i < l ; i ++ ) {
            if(sum >= i) {
                sum += a[i] - '0' ;
            }
            else {
                ans += i - sum ;
                sum = i + a[i] - '0' ;
            }
        }
        printf("Case #%d: %d\n", ++ ca , ans) ;
    }
    return 0 ;
}
