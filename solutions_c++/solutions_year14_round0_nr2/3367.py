#include <iostream>

using namespace std;

const char* input = "input.in";
const char* output = "output.out";

//#define debug(format, ...) printf(format, __VA_ARGS__)
#define debug(format, ...)

int main()
{
    freopen(input, "r", stdin);
    freopen(output, "w", stdout);

    int tc;
    cin >> tc;
    debug("N testcases = %d\n\n", tc);

    for (int test=1; test <= tc; ++test) {
        double c, f, x;
        cin >> c;
        cin >> f;
        cin >> x;

        debug("Test %d\n", test);
        debug("c = %f, f = %f, x = %f\n", c, f, x);

        double buildTime = 0;
        double noBuildCost = 0;
        double buildCost = 0;
        double cookieRate = 2;

        do {
            // First case: we don't build anything else
            noBuildCost = buildTime + x/cookieRate;

            // Second case: we build
            buildTime += c/cookieRate;
            cookieRate += f;
            buildCost = buildTime + x/cookieRate;

            debug("noBuildCost = %f, buildCost = %f\n", noBuildCost, buildCost);
        } while (buildCost < noBuildCost);

        printf("Case #%d: %f\n", test, noBuildCost);
    }

    return 0;
}

