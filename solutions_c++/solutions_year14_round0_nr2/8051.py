#include <cstdio>
#include <fstream>
using namespace std;

double duration(double speed, double quantity)
{
    return quantity / speed;
}

int main()
{
    ifstream input;    input.open("date.in");
    freopen("date.out", "w", stdout);
    int T;
    input >> T;

    for (int Case = 1; Case <= T; ++Case)
    {
        double C, F, X, current = 2, elapsed_time = 0;
        input >> C >> F >> X;
        while (duration(current, X) > duration(current, C) + duration(current + F, X))
            elapsed_time += duration(current, C), current += F;
        elapsed_time += duration(current, X);
        printf("Case #%d: %.7f\n", Case, elapsed_time);
    }
    return 0;
}
