#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T;

void output(int Case, double out)
{
    printf("Case #%d: %.7f\n", Case, out);


}

double run(double C, double F, double X)
{
    double nFarms = 0;
    double best = X/(2+nFarms*F);
    double nCookies = 0;
    double time = 0;
    while (nCookies < X && time < best)
    {
        if (nCookies < C)
        {
            time += (C-nCookies)/(2+nFarms*F);
            nCookies += (C-nCookies);
        }else if (nCookies >= C)
        {
            nFarms++;
            nCookies-=C;
            best = min(best, time + (X-nCookies)/(2+nFarms*F));
        }
    }

    return best;



}

int main()
{
    freopen("inFile.txt", "r", stdin);
    freopen("outFile.txt", "w", stdout);

    cin >> T;

    for (int Case = 1; Case <= T; Case++)
    {
        double C, F, X;
        cin >> C >> F >> X;
        double ans = run(C, F, X);
        output(Case, ans);
    }
    return 0;
}
