#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int sc = 0; sc < T; sc++) {
        double C, F, X;
        cin >> C >> F >> X;

        double best = X / 2.0;
        double sum = 0.0;
        long long i;
        for (i = 1; 1; i++) {
            sum += 1 / (2 + (i-1)*F);
            double cur = sum*C + X/(2+i*F);
            if (cur < best) best = cur; else break;
        }

        cout << "Case #" << sc+1 << ": ";
        cout << fixed << setprecision(7) << best;
        cout << endl;
    }
    
    return 0;
}
