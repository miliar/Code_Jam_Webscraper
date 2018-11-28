#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
    int tests;
    cin >> tests;
    string blank;
    getline(cin, blank);

    for (int t = 1; t <= tests; t++)
    {
        double f,c,x;
        cin >> c;
        cin >> f;
        cin >> x;
        getline(cin, blank);

        double time = 0;
        double p = 2;

        while ( (x / p) > ((c / p) + (x / (p + f))) ) {
            time += c / p;
            p += f;
        }
        time += x / p;


        printf("Case #%d: %.7f\n", t, time );
    }

    return 0;
}

