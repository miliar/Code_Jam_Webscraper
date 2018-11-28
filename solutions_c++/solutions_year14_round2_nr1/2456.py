#include<math.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

FILE *fin = fopen("solve.in","r");
FILE *fout = fopen("solve.out","w");

int main()
{
    int nn2[101], nn1[101];
    int tc, ans, n, l, i, j, ss2, ss1;
    char a[101], b[101], c2[101], c1[101];
    fscanf(fin,"%d",&tc);
    for(l=1; l<=tc; l++) {
        fscanf(fin,"%d",&n);
        fscanf(fin,"%s%s",a,b);
        ans = 0;

        ss1 = 0;
        memset(nn1,0,sizeof(nn1));
        nn1[ss1] = 1;
        c1[ss1++] = a[0];
        for(i=1; i<strlen(a); i++)
            if(a[i] != c1[ss1-1]) {
                nn1[ss1] = 1;
                c1[ss1++] = a[i];
            } else {
                nn1[ss1-1]++;
            }

        ss2 = 0;
        memset(nn2,0,sizeof(nn2));
        nn2[ss2] = 1;
        c2[ss2++] = b[0];
        for(i=1; i<strlen(b); i++)
            if(b[i] != c2[ss2-1]) {
                nn2[ss2] = 1;
                c2[ss2++] = b[i];
            } else {
                nn2[ss2-1]++;
            }

        if(ss1 != ss2) {
            fprintf(fout,"Case #%d: Fegla Won\n",l);
            continue;
        } else {
            int geldik=0;
            for(i=0; i<ss1; i++)
                if(c1[i] != c2[i]) {
                    fprintf(fout,"Case #%d: Fegla Won\n",l);
                    geldik = 1;
                    break;
                } else {
                    ans+=abs(nn1[i]-nn2[i]);
                }
            if(geldik) continue;
        }
        fprintf(fout,"Case #%d: %d\n",l,ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
