#include <cstdio>
#include <math.h>


using namespace std;


int n;
long long int r,t;

int main()
{
    FILE* be=fopen("A-small-attempt1.in","r");
    FILE* ki=fopen("out.txt","w");
    fscanf(be,"%d",&n);
    for(int c=0; c<n; c++)
    {
        fscanf(be,"%lld %lld",&r,&t);
        //printf("%lld %lld\n",r,t);
        int i=0;
        while (t>=0)
        {
            t-=2*r+1;
            r+=2;
            i++;
        }
        //fprintf(ki,"%f", 0.25*(sqrt(4*r*r-4*r+8*t+1)-2*r-3));
        fprintf(ki,"Case #%d: %d\n",c+1,i-1);
    }

    fclose(be);
    fclose(ki);
    return 0;
}
