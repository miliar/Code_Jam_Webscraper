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
        int r1, r2, a[4][4], b[4][4];
        cin >> r1;
        --r1;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j) cin >> a[i][j];
        cin >> r2;
        --r2;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j) cin >> b[i][j];
        set<int> F, S;
        for (int i = 0; i < 4; ++i) F.insert(a[r1][i]);
        for (int i = 0; i < 4; ++i)
            if (F.find(b[r2][i]) != F.end()) S.insert(b[r2][i]);
        cout << "Case #" << test << ": ";
        if (sz(S) == 1) cout << *S.begin() << endl;
        else if (sz(S) == 0) cout << "Volunteer cheated!" << endl;
        else cout << "Bad magician!" << endl;
    }

#ifdef harhro94
    cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
    return 0;
}