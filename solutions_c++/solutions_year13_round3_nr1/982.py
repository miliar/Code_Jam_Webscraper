#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int T;
char in[1000005];
int len;
int N;
int val[1000005];
int cv, *p;
long long ans, countt;

int main(){
    int i;

    freopen( "A-large.in", "r", stdin);
    freopen( "out.txt", "w", stdout);

    scanf("%d", &T);
    for( int tt = 1; tt <= T; tt++){
        cv = 0;
        scanf("%s %d", in, &N);
        len = strlen( in);

        ans = 0;
        countt = 0;
        for( i = 0; i < len; i++){
            if( in[i] == 'a' || in[i] == 'e' || in[i] == 'i' || in[i] == 'o' || in[i] == 'u'){
                countt = 0;
            }
            else countt++;

            if( countt >= N)val[cv++] = i;
        }

        for( i = 0; i < len; i++){
            p = lower_bound( val, val + cv, i + N - 1);
            if( cv > p - val)ans += (long long)(len - (*p));

        }

        printf("Case #%d: %lld\n", tt, ans);
    }
}
