#include<iostream>
#include<cstdio>
#include<float.h>
using namespace std;
int main()
{
    unsigned short T;
    double C,F,X;
    double time,gain,min;
    cin >> T;
    for ( int i = 0; i < T; i++ )
    {
        cin >> C >> F >> X;
        if ( C > X )
        {
            printf("Case #%d: %.7lf\n", i+1, X / 2.0d );
            continue;
        }
        min = DBL_MAX;
        for ( unsigned long tries = 0; true; tries++ )
        {
            time = 0.0d;
            gain = 2.0d;
            for ( unsigned long i = 0; i < tries; i++ )
            {
                time += C / gain; 
                gain += F;
            }
            time += X/gain;
            if ( min < time )
               break;
            min = time;
        }
        printf("Case #%d: %.7lf\n", i+1, min );
    }
}