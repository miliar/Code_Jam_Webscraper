#include<cstdio>
#include<cstdlib>
#include<iostream>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, tc;
    double C, F, X, rate;
    double ans, lgsg, beliLagi;

    cin >> T;

    for(tc=1;tc<=T;tc++)
    {
        cin >> C >> F >> X;

        ans = 0; rate = 2;

        do
        {
            lgsg = X/rate;
            beliLagi = C/rate + X/(rate+F);

            if(lgsg <= beliLagi)
            {
                ans += lgsg;
            }
            else
            {
                ans += C/rate;
                rate += F;
            }
        }while(lgsg > beliLagi);

        printf("Case #%d: %.7lf\n", tc, ans);
    }


    return 0;
}

