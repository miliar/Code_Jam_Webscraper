#include <iostream>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    
    for( int tt = 1; tt<=t; tt++ )
    {
        double c, f, x, curF, curTime;
        curF = 2.0;
        scanf("%lf %lf %lf", &c, &f, &x);
        
        curTime = 0;
        
        while( x/curF > c/curF + x/(f+curF) )
        {
            curTime += c/curF;
            curF += f;
        }
        
        printf("Case #%d: %.7lf\n", tt, curTime + x/curF);
    }
    
    return 0;
}