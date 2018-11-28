#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t, T, len, i, chang;
    char s[105];
    scanf("%d",&T);

    for ( t = 1 ; t <= T ; ++ t ) {
        scanf("%s",&s);
        len = strlen(s);
        chang = 0;
        for ( i = 1 ; i < len ; ++ i ) {
            if ( s[i] != s[i-1] )
                chang++;
        }

        if ( chang == 0 ) {
            printf("Case #%d: %d\n",t,s[0]=='+'?0:1);
        }
        else {
            printf("Case #%d: %d\n",t,chang+(s[len-1]=='-'?1:0));
        }
    }
    return 0;
}
