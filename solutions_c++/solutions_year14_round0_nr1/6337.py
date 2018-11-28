#include <cstdio>
#include <deque>
#include <queue>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <climits>
#include <cfloat>
#include <map>
#include <cstring>
#include <ctime>
#include <cassert>

#define MOD 1000000007
#define EPS 1e-9
#define INF 2117117117
#define LLINF 2117117117117117117LL
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define sqr(a) ((a) * (a))
#define sz(a) ((int) (a).size())

#define uNEG (ulong) -1
#ifndef M_PI
const double M_PI = acos(-1.0);
#endif

typedef unsigned int uint;
typedef long long llong;
typedef long double ldouble;
typedef unsigned long long ullong;

#define TASK "task"

using namespace std;

const int N = 4;

int q;
int arr[N][N], a, ans, ansc;
bool ha[sqr(N)], hb[sqr(N)];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //freopen(TASK".in", "r", stdin);
    //freopen(TASK".out", "w", stdout);

    //init + input
    scanf("%d", &q);

    //proc each test
    for (int qq = 0; qq < q; qq++)
    {
        memset(ha, false, sizeof(ha));
        memset(hb, false, sizeof(hb));
        scanf("%d", &a);
        a--;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                scanf("%d", &arr[i][j]);
        for (int i = 0; i < N; i++)
            ha[arr[a][i] - 1] = true;
        scanf("%d", &a);
        a--;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                scanf("%d", &arr[i][j]);
        for (int i = 0; i < N; i++)
            hb[arr[a][i] - 1] = true;
        ansc = 0;
        for (int i = 0; i < sqr(N); i++)
            if (ha[i] && hb[i])
            {
                ansc++;
                ans = i + 1;
            }
        printf("Case #%d: ", qq + 1);
        if (ansc == 0)
            printf("Volunteer cheated!\n");
        else if (ansc > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", ans);
    }

    return 0;
}
