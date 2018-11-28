#include <iostream>
#include <cstdio>
//#include <ifstream>

using namespace std;

int main()
{
    freopen("../B-large.in", "r", stdin);
    freopen("../b-large.out", "w", stdout);

    int T = 0;
    cin >> T;

    const double v = 2.0;

    for (int test_case = 1; test_case <= T; test_case++)
    {
        double C, F, X;
        cin >> C >> F >> X;

        double totalTime = 0;

        double currV = v;
        double nextBuy = C / currV;
        double waitTime = X / currV;

        for (;;)
        {
            if (waitTime < nextBuy || X / (currV + F) > (X - C) / currV)
            {
                totalTime += waitTime;
                break;
            }
            else
            {
                    totalTime += nextBuy;
                    currV += F;
                    nextBuy = C / currV;
                    waitTime = X / currV;
            }
        }

        cout << "Case #" << test_case << ": ";
        printf("%.7f\n", totalTime);
    }



    return 0;
}

