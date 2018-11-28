#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <list>

using namespace std;

const int MAX = 1e5;
const int INF = 1e9;
const double EPS = 1e-9;

int main() 
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        
        double minimum = x / 2.0;
        double cost = 0;
        double speed = 2.0;
        for(int i = 1; i <= x; ++i)
        {
            cost += c / speed;
            speed += f;
            minimum = min(minimum, cost + x / speed);
        }
        printf("Case #%d: %.7f\n", Ti, minimum);
    }

    return 0;
}

