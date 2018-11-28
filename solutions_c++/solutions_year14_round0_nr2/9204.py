#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int ii,n,t;
    double c,f,x,best,fromFarms;
    scanf ("%d",&t);
    for ( ii=1; ii<=t; ii++ )
    {
        scanf ("%lf%lf%lf",&c,&f,&x);
        
        fromFarms = 0;
        best = x / 2;
        n = 0;
        while (1)
        {
            fromFarms += c / (2 + (double)n*f);
            n++;
            if ( best > fromFarms + x / ( 2 + (double)n*f ) )
                best = fromFarms + x / ( 2 + (double)n*f );
            else break;
        }
        
        printf ("Case #%d: %.7f\n",ii,best);    
    }
}