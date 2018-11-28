#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
using namespace std;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;
const int MAX = 74;
const int MAX2 = 7000;
const int BASE = 1000000000;

int n;

bool d[10];

int solve(int x)
{
    int t = x;
    FILL(d, 0);
    while (1)
    {
        int y = x;
        if (y == 0)
            ++ d[0];
        while (y)
        {
            d[y % 10] = 1;
            y /= 10;
        }
        bool ok = 1;
        FOR (i,0,10)
            if (d[i] == 0)
                ok = 0;
        if (ok)
            return x;
        x += t;
    }
}


int main()
{
    freopen("A-large (4).in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;
    FOR (test,0,T)
    {
        int n;
        cin >> n;
        cout << "Case #" << test+1 << ": ";
        if (n == 0)
            cout << "INSOMNIA" << endl;
        else
            cout << solve(n) << endl;
    }

    return 0;
}
