#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <cctype>
#include <queue>
#include <complex>
#include <functional>
#include <sstream>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	double c, f, x;
    	cin >> c >> f >> x;
    	double t = 0;
        double cur = 2;
    	while (x / cur >= x / (cur + f) + c / cur)
        {
            t += c / cur;
            cur += f;
        }
        t += x / cur;
    	printf("Case #%d: %0.10lf\n", tc + 1, t);
    }
    return 0;
}