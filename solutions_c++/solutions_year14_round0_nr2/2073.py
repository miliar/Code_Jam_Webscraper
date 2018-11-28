#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;


void solve(int t)
{
    double c, f, x;
    cin >> c >> f >> x;

    double best = 1.0e20;
    for (int b = 0; b < x; b++)
    {
        double time = 0;
        double r = 2;

        for (int i = 0; i < b; i++)
        {
            time += c / r;
            r += f;
        }

        time += x / r;

        if (time > best)
            break;
        else
            best = time;
    }

    cout.precision(10);
    cout << fixed;
    cout << "Case #" << t+1 << ": " << best << endl;
    cerr << "case " << t+1 << endl;
}

int main(int argc, char *argv[])
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
        solve(i);

    return 0;
}
