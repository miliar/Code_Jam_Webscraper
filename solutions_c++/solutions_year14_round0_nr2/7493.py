#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
typedef long long int ll;

double c, f, x, fans , a, b, ans , s;
int t, p, tt;

int main()
{
    cin >> t;
    tt = 1;
    while (t--)
    {
        cin >> c >> f >> x;
        p = 0; ans = 0; s = 2;
        a = (c * (s + (f * (p + 1))) + x * (s + (f * p))) / ((s + (f * (p + 1))) * (s + (f * p)));
        b = (x / (s + (f * p)));
        while (a < b)
        {
            ans = (ans*(s + (f * p)) + c) / (s + (f * p));
            p++;
            a = (c * (s + (f * (p + 1))) + x * (s + (f * p))) / ((s + (f * (p + 1))) * (s + (f * p)));
            b = (x / (s + (f * p)));
        }
        ans = ans + b;
        printf("Case #%d: %.7f\n", tt++, ans);
    }
}
