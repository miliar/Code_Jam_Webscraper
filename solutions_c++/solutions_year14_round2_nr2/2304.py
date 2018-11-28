#include<stdio.h>

FILE *fin = fopen("solve.in","r");
FILE *fout = fopen("solve.out","w");

int main()
{
    int tc, ans;
    int a, b, k;
    int i, j, l;
    fscanf(fin,"%d",&tc);
    for(l=1; l<=tc; l++) {
        fscanf(fin,"%d%d%d",&a,&b,&k);
        ans = 0;
        for(i=0; i<a; i++)
        for(j=0; j<b; j++)
            if((i&j) < k)
                ans++;
        fprintf(fout,"Case #%d: %d\n",l,ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
