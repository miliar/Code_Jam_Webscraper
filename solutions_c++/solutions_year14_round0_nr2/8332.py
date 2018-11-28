#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int T;

double c, f, x;
const double eps = 1e-8;

int main()
{
    scanf("%d", &T);
    for (int t = 0; t < T; ++t)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        double res = 0.0;
        double rate = 2.0;
        while ( c + (x * rate)/ (rate + f) + eps < x )
        {
            
            res += c / rate;
            rate += f;
        }
        res += x / rate;
        printf("Case #%d: %.7f\n", t + 1, res);
    }
    return 0;
}