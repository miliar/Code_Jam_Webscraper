#include <stdio.h>

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int t, t1;
    unsigned long long n, tot, ttot, dChk, d;

    fscanf(fin,"%d", &t);
    t1 = 1;
    while(t1 <= t) {
        fscanf(fin,"%lld", &n);

        if(n == 0) { // INSOMNIA case
            fprintf(fout,"Case #%d: INSOMNIA\n", t1);
            t1++;
            continue;
        }

        tot = 0;
        dChk = 0;
        while(1) {
            tot += n;

            ttot = tot;
            while(ttot) {

                d = ttot%10;
                ttot = ttot/10;
                dChk = (dChk | (1<<d));
            }
            if(dChk == 1023) {
                break;
            }
        }

        fprintf(fout,"Case #%d: %d\n", t1, tot);
        t1++;
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
