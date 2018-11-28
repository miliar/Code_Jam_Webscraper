#include<stdio.h>

FILE *fin = fopen("solve.in","r");
FILE *fout = fopen("solve.out","w");

int main()
{
    int tc, i;
    double c, f, x;
    double spd, prev, cur, frm;
    fscanf(fin,"%d",&tc);
    for(i=1; i<=tc; i++) {
        fscanf(fin,"%lf%lf%lf",&c,&f,&x);
        prev = x/2.000;
        spd = 2;
        frm = 0;
        while(1) {
            frm+=((double)(c/spd));
            spd+=f;
            cur = (frm+((double)(x/spd)));
            if(prev < cur) break;
            prev = cur;
        }
        fprintf(fout,"Case #%d: %.7lf\n",i,prev);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
