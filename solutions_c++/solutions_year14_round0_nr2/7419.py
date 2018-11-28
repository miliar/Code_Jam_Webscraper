#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);
    int T;
    double ST = 2, C, F, X, Minimum, minMas;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> C >> F >> X;
        Minimum = X/ST;
        minMas = C/ST; ST += F;
        for (int j = 1; j < 10000000; j++) {
            if (Minimum > minMas + X/ST) {
                Minimum = minMas + X/ST;
                minMas += C/ST;
                ST += F;
            }
        }
        ST -= F;

        printf("Case #%d: %.7f\n", i+1, Minimum);
        minMas = 0;
        ST = 2; Minimum = 0;
    }


    return 0;
}
