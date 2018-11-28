#include <iostream>
#include <cmath>

int main(int argc, const char * argv[])
{
    freopen("/Users/yuristuken/Documents/codejam14/B/B/B-large.in", "r", stdin);
    freopen("/Users/yuristuken/Documents/codejam14/B/B/B-large.out", "w", stdout);
    int nTests;
    std::cin >> nTests;
    for (int test = 1; test <= nTests; ++test)
    {
        double c, f, x;
        std::cin >> c >> f >> x;
    
        int n = ceil(x/c - 2/f - 1);
    
        double currentPower = 2;
        double currentTime = 0;
        while (n > 0)
        {
            currentTime += c / currentPower;
            currentPower += f;
            --n;
        }
    
        currentTime += x / currentPower;
        printf("Case #%d: %.7f\n", test, currentTime);
    }
    return 0;
}

