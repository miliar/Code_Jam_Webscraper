#include <iostream>
#include <array>
#include <set>
#include <algorithm>
#include <cstdio>

using namespace std;

int main(int argc, char **argv, char **envp)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T; cin >> T;

    for(int t = 0; t < T; ++t)
    {
        double c, f, x;
        cin >> c >> f >> x;

        double rate = 2.0;

        double minTime = x / rate;

        double currTime = 0.0;

        for(int i = 0; i < 100000000; ++i)
        {
            currTime += c / rate;
            rate += f;
            minTime = std::min(minTime, currTime + x / rate);
        }
        fprintf(stderr, "%d\n", t);
        printf("Case #%d: %.10lf\n", t + 1, minTime);
    }

    return 0;
}