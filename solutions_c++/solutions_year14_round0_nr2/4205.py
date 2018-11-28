#include <iostream>
#include <stdio.h>
using namespace std;
FILE *fin,*fout;
double C,F,X;
double total,sol,sol1,cate;
void solve()
{
    double aux;
    sol=X/2; cate=2; sol1=0;
    int ferme=0;
    while(ferme<X)
    {
       total=sol1+X/cate;
       if(sol-total > 0.0000001) sol=total;
        aux= C/cate;
        ferme++;
       sol1+=aux;
       cate+=F;
    }
    fprintf(fout,"%.7lf\n",sol);
}
int main()
{
    int t;
    fin=fopen("t.in","r");
    fout=fopen("output.txt","w");
    fscanf(fin,"%d",&t);
    for(int i=1;i<=t;i++)
    {
        fscanf(fin,"%lf%lf%lf",&C,&F,&X);
        fprintf(fout,"Case #%d: ",i);
        solve();
    }
    return 0;
}
