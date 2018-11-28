#include<cstdio>
char matrix[4][4][4]={'G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G',
                    'R','G','R','G','G','G','G','G','R','G','R','G','G','G','G','G',
                    'R','R','R','R','R','R','G','R','R','G','G','G','R','R','G','R',
                    'R','R','R','R','R','R','R','R','R','R','R','G','R','R','G','G'};
//x, r, c
int main()
{
    int x, r, c, t;
    FILE *fin, *fout;
    fin = fopen("D-small-attempt4.in","r");
    fout = fopen("D(1).out","w");
    fscanf(fin,"%d",&t);
    for(int i = 1; i <= t; i++)
    {
        fscanf(fin,"%d%d%d",&x,&r,&c);
        switch (matrix[x-1][r-1][c-1])
        {
            case 'G':fprintf(fout,"Case #%d: GABRIEL\n",i);break;
            case 'R':fprintf(fout,"Case #%d: RICHARD\n",i);break;
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
