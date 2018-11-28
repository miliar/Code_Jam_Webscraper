#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    FILE *fin,*fout;
    fin=fopen("input.txt","r");
    fout=fopen("output.txt","w");
    int T;
    fscanf(fin,"%d",&T);
    for (int t1=0;t1<T;t1++)
    {
        double c,f,x,pl=2,cookies=0,t=0,rez;
        fscanf(fin,"%lf %lf %lf", &c, &f, &x);
        rez=9999999999;
        while (t<rez)
        {
            rez=min(rez,t+x/pl);
            t=t+(c-cookies)/pl;
            pl+=f;
        }
        fprintf(fout,"Case #%d: %.7lf\n",t1+1,rez);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
