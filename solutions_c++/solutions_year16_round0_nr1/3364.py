//
// Created by Acka on 4/9/16.
//

#include <stdio.h>

int main()
{
    freopen("/Users/acka/ClionProjects/ProblemSolving/A-large.in", "r", stdin);
    freopen("/Users/acka/ClionProjects/ProblemSolving/A-large.out", "w", stdout);

    int tc, st = 1; for(scanf("%d", &tc); tc--;){
        int n; scanf("%d", &n);

        bool chk[10] = {false,};
        int cnt = 0, loop = 1000, x = n, copy, last;
        while(--loop){
            copy = x;
            while(copy){
                last = copy % 10;
                if(!chk[last]){
                    chk[last] = true;
                    cnt++;
                }
                copy /= 10;
            }

            if(cnt == 10) break;
            x += n;
        }

        if(loop) printf("Case #%d: %d\n", st++, x);
        else printf("Case #%d: INSOMNIA\n", st++);
    }
    return 0;
}