// Author: Harhro94 [Harutyunyan Hrayr]
#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef long double LD;
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

const LD eps = 1e-9;

int main()
{
#ifdef harhro94
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#define task ""
    //freopen(task".in", "r", stdin);
    //freopen(task".out", "w", stdout);
#endif

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        cout << "Case #" << test << ": ";

        LD C, F, X;
        cin >> C >> F >> X;

        LD rate = 2.0;
        LD ans = 1e18;
        LD curTime = 0.0;
        for (int i = 0; i <= 1000000; ++i)
        {
            ans = min(ans, curTime + X / rate);
            curTime += C / rate;
            rate += F;
        }

        cout << fixed << setprecision(9) << ans << endl;
    }

#ifdef harhro94
    cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
    return 0;
}