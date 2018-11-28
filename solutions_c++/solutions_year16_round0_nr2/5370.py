#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int t, t1, ln;
    int bcki, frti, i;
    int ans;
    char tmp;
    char stk[102];
//    char *stk;
//    stk = (char*) malloc(sizeof(char));

    fscanf(fin, "%d",&t);
    t1 = 1;
    while(t1 <= t) {

        fscanf(fin, "%s", stk);
        ln = strlen(stk);
        ans = 0;

        bcki = ln-1;
        while(bcki > -1) {

            if(stk[bcki] == '+') {
                bcki--;
                continue;
            }

            //prepare for flip prefix
            frti = 0;
            while(stk[frti] == '+' && frti < bcki) {
                stk[frti] = '-';
                frti++;
            }
            if(frti > 0) ans++;

            //flip prefix till bcki
            ans++;
            for(i=0; i<=bcki; i++) {
                if(stk[i] == '+') stk[i] = '-';
                else stk[i] = '+';
            }
            for(i=0; i<=bcki/2; i++) {
                tmp = stk[i];
                stk[i] = stk[bcki-i];
                stk[bcki-i] = tmp;
            }

            bcki--;
        }

        fprintf(fout, "Case #%d: %d\n", t1, ans);
        t1++;
    }

//    free(stk);
    fclose(fin);
    fclose(fout);
    return 0;
}
