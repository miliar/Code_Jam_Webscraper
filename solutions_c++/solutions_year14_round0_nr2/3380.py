//
//  main.cpp
//  GoogleCodeJam2014
//
//  Created by Shahab Uddin on 4/12/14.
//  Copyright (c) 2014 Shahab Uddin. All rights reserved.
//

#include <iostream>
#include <cstring>

#define LL long long
#define EPS 0.00000001

void print(double p, int c)
{

     printf ("Case #%d: %.7lf\n", c, p);
}

int main(int argc, const char * argv[])
{
    freopen("/Users/Shahab/Documents/Sourcecode/CPP/GoogleCodeJam2014/GoogleCodeJam2014/Cookie_Clicker_Alpha/large_input.txt", "r", stdin);
    freopen("/Users/Shahab/Documents/Sourcecode/CPP/GoogleCodeJam2014/GoogleCodeJam2014/Cookie_Clicker_Alpha/large_output.txt", "w", stdout);

    int testCases;

    scanf ("%d", &testCases);

    int cases = 1;

    while ( testCases-- ) {

        double c, f, x;

        scanf ("%lf %lf %lf", &c, &f, &x);

        double retTime = 0;

        if (x <= c) {
            print(x / 2.0, cases);
        } else {

            int factoryCount = 0;

            while (1) {
                retTime += (c / (2.0 + (factoryCount * f)));

                double tmpTime = ((x - c) / (2.0 + (factoryCount * f)));
                double factoryTime = (x / (2.0 + ((factoryCount + 1) * f)));

                if (tmpTime < factoryTime) {
                    print(retTime + tmpTime, cases);
                    break;
                } else {
                    factoryCount++;
                }
            }
        }

        cases++;

    }

    return 0;
}


