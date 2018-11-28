#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#define pb push_back
using namespace std;

void solve(int tc)
{
    cout << "Case #" << tc << ": ";
    double C, F, X;
    double rate = 2.0;
    cin >> C >> F >> X;
    double best = 0.0, cr, sc = 0.0;
    int v = X / C, l;
    for(l = 0; l <= v; ++l)
    {
        if(l > 0) sc += C / (2.0 + (l - 1) * F);
        cr = sc + X / (2.0 + l * F);
        if(l == 0) best = cr;
        best = min(best, cr);
    }
    printf("%.8lf\n", best);
}

map<char, char> R;

int main()
{
    int tc, t;
    cin >> t;
    for(tc = 1; tc <= t; ++tc) solve(tc);
}

