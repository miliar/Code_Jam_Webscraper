#include<stdio.h>
#include<algorithm>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

double c , f , ff , x;

double solve()
{
    int i;
    double ret = 0 , req;
    
    for(i=0;;i++)
    {
        req = (c / ff) + (x / (ff + f));
    
        if((x / ff) <= req)
        {
            ret += (x / ff);
            break;
        }
    
        ret += (c / ff);
        ff += f;
    }
    return ret;
}

int main()
{
    int i , a , cases , caseID = 0;
    
    fscanf(in,"%d",&cases);
    while(cases--)
    {
        ff = 2.0;
        fscanf(in,"%lf %lf %lf",&c,&f,&x);
        fprintf(out,"Case #%d: %.7lf\n",++caseID,solve());
    }
        
    return 0;
}
