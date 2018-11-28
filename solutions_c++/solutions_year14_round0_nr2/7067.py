#include <iostream>
#include <cstdio>

using namespace std;

double C, F, X;

double Solve()
{
    double time = 0.0;
    double pc = 2.0;

    while (true) {
        double c1 = X / pc;
        double c2 = X / (pc + F) + (C / pc);

        if (c1 < c2)
            return time + c1;

        time += C / pc;
        pc += F;
    }
}

int main()
{
    int T;

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> C >> F >> X;
        printf("Case #%d: %.8f\n", t, Solve());
    }

    return 0;
}
