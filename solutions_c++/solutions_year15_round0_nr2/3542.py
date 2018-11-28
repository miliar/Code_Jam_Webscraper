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
typedef unsigned long long UInt;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;
const int MAX = 1024;
const int MAX2 = 200007;
const int BASE = 1000000000;

double eps = 1E-7;

int n;
int A[MAX];

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-large (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);


    int T;
    scanf("%d", &T);
    FOR (test,0,T)
    {
        cin >> n;
        FOR (i,0,n)
            cin >> A[i];
        int mx = 0;
        FOR (i,0,n)
            mx = max(mx, A[i]);
        int res = mx;
        FOR (i,1,mx+1)
        {
            int cnt = i;
            FOR (j,0,n)
            {
                int add = (A[j] / i);
                if (A[j] % i == 0)
                    -- add;
                cnt += add;
            }
            res = min(res, cnt);
        }
        cout << "Case #" << test+1 << ": " << res << endl;
    }


    return 0;
}
