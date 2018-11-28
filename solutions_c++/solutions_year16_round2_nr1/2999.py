#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int t, t1;
    char ss[2001];

    int i, j, l;
    int ans[10];
    int cnt[28];

    fscanf(fin, "%d", &t);
    t1 = 1;
    while(t1 <= t) {
        fscanf(fin, "%s", ss);

        // set to default
        for(i=0; i<10; i++) { ans[i] = 0; }
        for(i=0; i<28; i++) { cnt[i] = 0; }

        //pre-calc counter
        l = strlen(ss);
        for(i=0; i<l; i++) cnt[ss[i] - 'A']++;

        /* calculate the answer */
        //Zero
        ans[0] = cnt[25];
        cnt[4] -= cnt[25];
        cnt[17] -= cnt[25];
        cnt[14] -= cnt[25];

        //tWo
        ans[2] = cnt[22];
        cnt[14] -= cnt[22];
        cnt[19] -= cnt[22];

        //foUr
        ans[4] = cnt[20];
        cnt[5] -= cnt[20];
        cnt[17] -= cnt[20];
        cnt[14] -= cnt[20];

        //siX
        ans[6] = cnt[23];
        cnt[8] -= cnt[23];
        cnt[18] -= cnt[23];

        //eiGht
        ans[8] = cnt[6];
        cnt[8] -= cnt[6];
        cnt[7] -= cnt[6];
        cnt[4] -= cnt[6];
        cnt[19] -= cnt[6];

        //ONE
        while(cnt[14] && cnt[13] && cnt[4]) {
            ans[1]++;
            cnt[4]--;
            cnt[13]--;
            cnt[14]--;
        }

        //THREE
        while(cnt[19] && cnt[7] && cnt[17] && cnt[4]>1) {
            ans[3]++;
            cnt[19]--;
            cnt[7]--;
            cnt[17]--;
            cnt[4] -=2;
        }

        //FIVE
        while(cnt[5] && cnt[8] && cnt[21] && cnt[4]) {
            ans[5]++;
            cnt[5]--;
            cnt[8]--;
            cnt[21]--;
            cnt[4]--;
        }

        //SEVEN
        while(cnt[18] && cnt[21] && cnt[13] && cnt[4]>1) {
            ans[7]++;
            cnt[18]--;
            cnt[13]--;
            cnt[21]--;
            cnt[4] -=2;
        }

        //NINE
        while(cnt[4] && cnt[8] && cnt[13]>1) {
            ans[9]++;
            cnt[8]--;
            cnt[4]--;
            cnt[13] -=2;
        }

        fprintf(fout, "Case #%d: ", t1);
        for(i=0; i<10; i++) {

            for(j=0; j<ans[i]; j++) {

                fprintf(fout, "%d", i);
            }
        }
        fprintf(fout, "\n");

        t1++;
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
