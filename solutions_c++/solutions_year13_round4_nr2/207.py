#include "stdio.h"
#include "stdlib.h"
#include "string.h"
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

typedef double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

int main()
{
    int T;
    cin >> T;
    for (int sc = 0; sc < T; sc++) {
        int i;
        TT n, p;
        cin >> n >> p;

        TT deg[60];
        deg[0] = 1;
        for (i = 1; i < 60; i++)
            deg[i] = deg[i-1] * 2;

        TT worst_place = 0;
        TT A = 0;
        for (i = 1; i <= n; i++) {
            worst_place += deg[n-i];
            if (worst_place >= p) break;
            A += deg[i];
            if (A > deg[n]-1) A = deg[n]-1;
        }

        TT B = 0;
        TT best_place = 0;
        for (i = 1; i <= n; i++) {
            best_place += deg[i-1];
            if (best_place >= p) break;
            B += deg[n-i];
        }

        cout << "Case #" << sc+1 << ": ";
        cout << A << " " << B;
        cout << endl;
    }

     return 0;
}
