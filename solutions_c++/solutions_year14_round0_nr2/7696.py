#include<stdio.h>
#include<algorithm>

using namespace std;

int main () {
    
    int tests;
    scanf("%d",&tests);
    
    for ( int ii = 1 ; ii <= tests ; ++ii ){
        
        double C,F,X;
        scanf("%lf %lf %lf",&C,&F,&X);
        
        double speed = 2;
        double elapsed = 0;
        for ( ; ; ){
            
            if ( X / speed > (C/speed) + X/(speed+F) ){
                elapsed += C/speed;
                speed += F;
            }
            else    break ;
        }

        printf("Case #%d: %.7lf\n",ii,elapsed+X/speed);
    }

    return 0;
}
