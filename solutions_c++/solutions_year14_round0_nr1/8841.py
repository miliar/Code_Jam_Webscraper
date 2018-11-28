#include <stdio.h>
#include <string.h>

FILE *fin = fopen("solve.in","r");
FILE *fout = fopen("solve.out","w");

int main()
{
    int ans;
    int t, a1, i, j, l;
    int m1[5][5], cnt[17];

    fscanf(fin,"%d",&t);
    for(l=1; l<=t; l++){
        memset(cnt,0,sizeof(cnt));

        fscanf(fin,"%d",&a1);
        for(i=1; i<5; i++)
        for(j=1; j<5; j++)
            fscanf(fin,"%d",&m1[i][j]);
        for(i=1; i<5; i++)
            cnt[m1[a1][i]]++;

        fscanf(fin,"%d",&a1);
        for(i=1; i<5; i++)
        for(j=1; j<5; j++)
            fscanf(fin,"%d",&m1[i][j]);
        for(i=1; i<5; i++)
            cnt[m1[a1][i]]++;

        j = 0;
        for(i=1; i<17; i++) {
            if(cnt[i]==2) {
                if(j == 1) {
                    j=2;
                    break;
                }
                j=1;
                ans = i;
            }
        }
        fprintf(fout,"Case #%d: ",l);
        if(j==0) {
            fprintf(fout,"Volunteer cheated!\n");
        } else
        if(j==1) {
            fprintf(fout,"%d\n",ans);
        } else
        if(j==2) {
            fprintf(fout,"Bad magician!\n");
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
