#include<stdio.h>
#include<string.h>

char name[1000001];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-out.txt", "w", stdout);
    int t, n, x;
    int i, j, l;
    long long y;
    int vowel[256];
    for(i = 0; i < 256; i++) vowel[i] = 0;

    vowel['a'] = 1;
    vowel['e'] = 1;
    vowel['i'] = 1;
    vowel['o'] = 1;
    vowel['u'] = 1;

    scanf("%d", &t);

    int last, seg, ok;
    for(x = 1; x <= t; x++) {
        scanf(" %s %d", name, &n);
        l = strlen(name);
        last = l-1;
        seg = 0;
        ok = 0;
        y = 0;
        for(i = l-1; i >= 0; i--) {
            if(vowel[ name[i] ] == 0) {
                seg++;
            }
            else {
                seg = 0;
            }
            if(seg >= n) {
                j = i+n-1;
                ok = 1;
            }
            if(ok){
                y = (long long) y + (l-j);
            }
        }
        printf("Case #%d: %I64d\n", x, y);
    }
    return 0;
}
