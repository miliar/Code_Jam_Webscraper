#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int in = 10000000;
int ans1, ans2, n, a[1111], b[1111];
double now;
int main(){         freopen("D-large.in", "r", stdin);
                    freopen("D-large.out","w", stdout);
    int T, tt;
    scanf("%d", &T);
    for(tt=1; tt<=T; tt++){
        scanf("%d", &n);
        int x, y;
        for(int i=0; i<n; i++){
            scanf("%lf", &now);
            a[i] = now*in;
        }
        for(int i=0; i<n; i++){
            scanf("%lf", &now);
            b[i] = now*in;
        }
        sort(a, a+n);
        sort(b, b+n);
        ans1 = ans2 = 0;
        for(int i=0, flag=0; i<n; i++){
            while( flag<n && a[flag]<=b[i] )    flag++;
            if( flag>=n )   break;
            else            ans1++;
            flag++;
        }
        for(int i=0, flag=0; i<n; i++){
            while( flag<n && b[flag]<=a[i] )    flag++;
            if( flag>=n )   break;
            else            ans2++;
            flag++;
        }
        ans2 = n-ans2;
        printf("Case #%d: %d %d\n", tt, ans1, ans2);
    }
    return 0;
}
