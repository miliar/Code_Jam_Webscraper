#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        double F, C, X;
        cin >> C >> F >> X;
        double best  = 0;
        double penalty = 0;
        double rate = 2.0;
        do 
        {
            best = X / rate + penalty;
            penalty += C / rate;
            rate += F;
        } while (best > penalty + (X / rate));
        printf("Case #%d: %.9f\n", t, best);
    }
    return 0;
}