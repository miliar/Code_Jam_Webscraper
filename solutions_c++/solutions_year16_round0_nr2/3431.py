//
// Created by Acka on 4/9/16.
//

#include <stdio.h>
#include <string.h>

int main()
{
    freopen("/Users/acka/ClionProjects/ProblemSolving/B-large.in", "r", stdin);
    freopen("/Users/acka/ClionProjects/ProblemSolving/B-large.out", "w", stdout);

    char s[101];
    int tc, st = 1; for(scanf("%d", &tc); tc--;){
        scanf("%s", s);

        int l;
        for(l = strlen(s) - 1; 0 <= l; l--)
            if(s[l] != '+') break;


        int ans = (l < 0 ? 0 : 1);
        for(int i = 1; i <= l; i++)
            if(s[i] != s[i - 1]) ans++;

        printf("Case #%d: %d\n", st++, ans);
    }
    return 0;
}