#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

void comeAndPlay()
{
    // C - cost of a factory
    // F - extra cookies per click
    // X - final amount of cookies
    double C, F, X, solution;
    cin >> C >> F >> X;

    // t1 - primitve
    // t2 - with a factory
    double t1, t2, T = 0.0;
    double production = 2.0;

    while (true) {
        t1 = X/production;
        t2 = C/production + X/(production+F);

        if (t1 < t2) {
            solution = T + t1;
            break;
        }

        T += C/production;
        production += F;
    }

    printf("%.7f", solution);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;
    for (int k = 1; k <= n; k++) {
        cout << "Case #" << k << ": ";
        comeAndPlay();
        cout << endl;
    }

    return 0;
}

