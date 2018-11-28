#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;

double C,F,X;

void ans_it()
{
    double production = 2.0;
    double t = 0;

    while ( true )
    {
        // printf ( "%lf %lf %lf %lf\n", X/production ,C/production , X/(production+F), t );
        if ( X/production <= C/production + X/(production+F) )
        {
            printf( "%.7lf\n", X/production + t );
            break;
        }
        else
        {
            t += C/production;
            production += F;
        }
    }
}

int main()
{
    int case_count = 0;
    cin >> case_count;
    for ( int i = 0; i < case_count; ++i )
    {
        cin >> C >> F >> X;
        cout << "Case #" << i + 1 << ": ";
        ans_it();
    }
    return 0;
}
