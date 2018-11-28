#include <iostream>
#include <stdio.h>
#include <vector>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void pro()
{
    double c,f,x;
    fscanf(fin,"%lf",&c);
    fscanf(fin,"%lf",&f);
    fscanf(fin,"%lf",&x);

    double overall=0,g=2;
    if(x>c)
    {
        while(1)
        {
            if((x/(g+f))<((x-c)/g))
            {
                overall+=(c/g);
                g+=f;
            }
            else
            {
                overall+=(x/g);
                break;
            }
        }
    }
    else
        overall=x/g;
    fprintf(fout,"%.7lf\n",overall);
}
int main()
{
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        pro();
    }
    return 0;
}
