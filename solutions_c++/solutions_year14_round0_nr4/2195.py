#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX 1000 + 10
using namespace std;

double a[MAX];
double b[MAX];

int f( int n)
{
    int ap = 0, ar = n - 1;
    int bp = 0, br = n - 1;
    int ans = 0;

    for ( int i = 0; i < n; i ++){
        if ( a[ar] < b[br]){
            ap ++;
            br --;
        }
        else{
            ar --;
            br --;
            ans ++;
        }
    }

    return ans;
}

int ff( int n)
{
    int ap = 0, ar = n - 1;
    int bp = 0, br = n - 1;
    int ans = 0;

    for ( int i = 0; i < n; i ++){
        if ( b[br] < a[ar]){
            bp ++;
            ar --;
            ans ++;
        }
        else{
            br --;
            ar --;
        }
    }

    return ans;
}

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t, cc = 1;
    scanf("%d", &t);

    while ( t --){
        memset( a, 0, sizeof(a));
        memset( b, 0, sizeof(b));
        int n, y = 0, z = 0;
        scanf("%d", &n);

        for ( int i = 0; i < n; i ++){
            scanf("%lf", &a[i]);
        }
        for ( int i = 0; i < n; i ++){
            scanf("%lf", &b[i]);
        }

        sort( a, a + n);
        sort( b, b + n);

        y = f( n);
        z = ff( n);

        printf("Case #%d: %d %d\n", cc, y, z);

        cc ++;
    }

    return 0;
}
