#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <memory.h>

using namespace std;

const int maxn = 1100;
int n;
int a[maxn];
int r[maxn], l[maxn];
int main()
{
    freopen("Blarge.in", "r", stdin );
    freopen("Blarge.out", "w", stdout );
    int t, tno = 0;
    cin>>t;
    while( t-- ){
        cin>>n;
        memset(r, 0, sizeof(r));
        memset(l, 0, sizeof(l));
        for(int i = 0; i < n; ++i){
            cin>>a[i];
        }
        int res = 0;
        for(int i = 0; i < n; ++i){
            for(int j = i + 1; j < n; ++j)
                if( a[j] > a[i] ) r[i]++;
            for(int j = 0; j < i; ++j )
                if( a[j] > a[i] ) l[i]++;
            res += min(l[i], r[i] );
        }
        printf("Case #%d: %d\n", ++tno, res);

    }
    return 0;
}
