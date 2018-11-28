#include <bits/stdc++.h>

using namespace std;

struct Party {
    int pName;
    int nSnt;
};
Party snts[27];

void sortIt(int nsnt)
{
    int i, j;
    Party tmps;
    for(i=0; i<nsnt; i++)
        for(j=i+1; j<nsnt; j++)
            if(snts[i].nSnt < snts[j].nSnt) {
                tmps.nSnt = snts[i].nSnt;
                tmps.pName = snts[i].pName;
                snts[i].nSnt = snts[j].nSnt;
                snts[i].pName = snts[j].pName;
                snts[j].nSnt = tmps.nSnt;
                snts[j].pName = tmps.pName;
            }
}

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int t1, t;
    int n, i, j;

    fscanf(fin, "%d", &t);
    t1 = 1;
    while(t1 <= t) {
        fprintf(fout, "Case #%d:", t1);

        fscanf(fin, "%d", &n);
        for(i=0; i<n; i++) {

            snts[i].pName = i;
            fscanf(fin, "%d", &snts[i].nSnt);
        }

        sortIt(n);

        while(1) {
            if(n == 2) break;

            for(i=0; i<n-1; i++) {
                if(snts[i].nSnt > snts[i+1].nSnt) {
                    break;
                }
            }

            fprintf(fout, " %c", 'A' + snts[i].pName);
            snts[i].nSnt--; //escaping

            if(snts[n-1].nSnt == 0) {
                n--;
            }
        }

        while(snts[0].nSnt > 0) {
            fprintf(fout, " %c%c", 'A' + snts[0].pName, 'A' + snts[1].pName);
            snts[0].nSnt--;
            snts[1].nSnt--;
        }

        fprintf(fout, "\n");
        t1++;
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
