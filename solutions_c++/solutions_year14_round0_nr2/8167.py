#include <bits/stdc++.h>

using namespace std;

double T;
double C, F, X;
double n;
double t, prevResult, result;
double time1, res1;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    cin >> T;

    for(int test = 1; test <= T; test++)
    {
        cin >> C >> F >> X;

        time1 = X/2;
        res1 = C/2 + X/(2+F);

        if(time1 < res1)
            printf("Case #%d: %.7f\n",test, X/2);
        else
        {
            t = 0;
            n = 0;
            prevResult = INFINITY;

            t = t + C/(2+n*F);
            result = t + X/(2+(n+1)*F);
            n++;

            while(result <= prevResult)
            {
                prevResult = result;

                t = t + C/(2+n*F);
                result = t + X/(2+(n+1)*F);

                n++;

            }

            printf("Case #%d: %.7f\n",test, prevResult);


        }


    }


    return 0;
}
