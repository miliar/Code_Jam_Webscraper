#include <iostream>
#include <cstdio>
#include <set>
using namespace std;
int main()
{
    freopen("B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    int test_case = 1;
    while( test_case <= T )
    {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);

        double step = 2;
        double sec1 = 0, sec2;
        double sum = 0;

        set <double> s;
        s.insert((double)X/step);

        while( 1 )
        {
            double secToC = (double)C/step;

            sec1 += secToC;
            step += F;
            sec2 = sec1 + (double)X/step;

            s.insert(sec2);

            if( sec2 > *s.begin() )  break;
        }
        printf("Case #%d: %.7lf\n", test_case, *s.begin());

        test_case++;
        s.clear();
    }

    return 0;
}
