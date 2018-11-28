#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <memory.h>

using namespace std;

const int maxn = 1e6 + 10;
int f[maxn];
int n, X;


int main(){
    freopen("A1.in", "r", stdin );
    freopen("A1.out", "w", stdout );
    int t;
    cin>>t;
    int tno = 0;
    while( t-- ){
        cin>>n>>X;
        for(int i = 0; i < n; ++i)
            scanf("%d", &f[i] );
        sort(f, f + n, greater<int>() );
        int be = 0, ed = n - 1;
        int tot = 0;
        for(; be <= ed; ){
            if( be == ed ){
                tot++; break;
            }
            if( f[be] + f[ed]> X ){
                be++;   tot++;
            }else{
                be++;   ed--;
                tot++;
            }
        }
        printf("Case #%d: %d\n", ++tno, tot);

    }
    return 0;
}
