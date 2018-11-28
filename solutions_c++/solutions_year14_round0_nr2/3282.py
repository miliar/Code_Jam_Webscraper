#include <iostream>
#include <stdio.h>

using namespace std;

double getBestSolution( double farmPrice, double cps, double goal )
{
    double prevTime = 0.0;
    double curTime = 0.0;
    double curDay = 0.0;

    double totPrevTime = 0.0;
    double totCurTime = 0.0;

    do
    {
        prevTime = curTime;
        curTime = prevTime + ( farmPrice / ( curDay*cps + 2.000000 ) );

        totPrevTime = prevTime + ( goal / (curDay*cps + 2.00000000 ) );
        totCurTime = curTime + ( goal / ( (++curDay)*cps + 2.00000000 ) );

    } while ( totPrevTime > totCurTime );

    return totPrevTime;
}

int main()
{
    int testCases = 0;
    double farmPrice = 0;
    double cps = 0;
    double goal = 0;

    cin >> testCases;
    double *myArray = new double[ testCases ];

    for ( int i = 0; i < testCases; ++i )
    {
        cin >> farmPrice >> cps >> goal;
        myArray[i] = getBestSolution( farmPrice, cps, goal );
    }

    for ( int i = 0; i < testCases; ++i )
    {
        printf( "Case #%d: %f\n", i+1, myArray[i] );
    }
}
