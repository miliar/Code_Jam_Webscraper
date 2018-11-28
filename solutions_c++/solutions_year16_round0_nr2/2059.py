#include <cstdio>

using namespace std;

int main() {
    int t,eeeeee;
    scanf("%d",&t);
    eeeeee=t;
    while ( t-- ) {
        char _s[103];
        scanf("\n%s",_s);
        char *s = _s+1;
        int w = 0;
        while ( *s ) {
            if (*s!=*(s-1)) w++;
            s++;
        }
        if (*(s-1)=='-') w++;
        printf("Case #%d: %d\n",eeeeee-t,w);
    }
    return 0;
}

