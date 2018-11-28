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


int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-large (4).in", "r", stdin);
    freopen("out.txt", "w", stdout);


    int T;
    cin >> T;
    FOR (test,0,T)
    {
        string s;
        cin >> s;
        int pos = 0, ans = 0;
        while (pos < SZ(s))
        {
            if (s[pos] == '+')
            {
                ++ pos;
                continue;
            }
            if (pos == 0)
                ++ ans;
            else
                ans += 2;
            int add = 1;
            while (pos+add < SZ(s) && s[pos+add] == '-')
                ++ add;
            pos += add;
        }
        cout << "Case #" << test+1 << ": " << ans << endl;
    }

    return 0;
}
