#include <cstdio>
#include <cstring>

char st[120]; int t,tc, sw, j;
char stc[100];
int main() {
    int n, i;
    scanf(" %d", &n);
    for(i=1;i<=n;i++) {
        scanf(" %s", st); t = strlen(st);
        tc=0;
        stc[tc] = st[0];
        for(j=1;j<t;j++) {
            while(j<t && st[j] == stc[tc]) j++;
            if(j<t)
                stc[++tc] = st[j];                                         
        }
        sw=0;
        tc++;
        for(j=0;j<tc;j++) {
            if(stc[j] == '+' && j+1<tc) sw++;
            else if(stc[j] == '-') sw++;
        }
        printf("Case #%d: %d\n", i, sw);
    }
    
    return 0;
}