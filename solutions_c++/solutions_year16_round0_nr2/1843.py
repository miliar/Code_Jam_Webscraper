#include <bits/stdc++.h>

#define size(n) ( int( n.size() ) )
#define sqr(n) ( (n) * (n) )

using namespace std;

const int N = 110;

char s[N];
int a[N];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d\n",&t);
    int k, i, len, curr, cnt;
    for ( k = 1; k <= t; k++ ){
        gets( s + 1 );
        len = strlen( s + 1 );
        for ( i = 1; i <= len; i++ ){
            a[i] = 0;
            if ( s[i] == '+' ){
                a[i] = 1;
            }
        }
        printf("Case #%d: ",k);
        cnt = 0;
        for ( i = len; i >= 1; i-- ){
            curr = ( cnt + a[i] ) % 2;
            if ( curr == 0 ){
                cnt++;
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}
