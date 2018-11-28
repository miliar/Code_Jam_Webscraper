#include<stdio.h>


int main(int argc, char** argv)
{
    FILE *file = fopen("tic.in","r"); 
    FILE *out = fopen("tic.out","w");
    int n=0;
    fscanf(file,"%d",&n);

    for(int i=0; i<n; ++i)
    {
        double C,F,X;
        fscanf(file,"%lf%lf%lf",&C,&F,&X);
        fprintf(out,"Case #%d: ",i+1);
        
        double s = 0.0;
        double n=0;
        double rate = 2.0;
        while( F*X / (2.0+(n+1)*F) > C)
        {
            s += C/rate;
            rate = rate+F;
            n++;
        }
        s+= X/rate;
        fprintf(out,"%.7lf\n",s);

    }

    fclose(file);
    fclose(out);
    return 0;
}
