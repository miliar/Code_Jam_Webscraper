#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int N_MAX = 2005;

int N, A[N_MAX], B[N_MAX], X[N_MAX];

void initialize()
{

}

bool go(int num)
{
    if (num > N)
        return true;

    int A_should[N], B_should[N];
    A_should[0] = 1;

    for (int i = 1; i < N; i++)
        A_should[i] = max(A_should[i - 1], X[i - 1] == 0 ? 0 : A[i - 1] + 1);

    B_should[N - 1] = 1;

    for (int i = N - 2; i >= 0; i--)
        B_should[i] = max(B_should[i + 1], X[i + 1] == 0 ? 0 : B[i + 1] + 1);

    for (int i = 0; i < N; i++)
        if (X[i] == 0 && A[i] == A_should[i] && B[i] == B_should[i])
        {
            X[i] = num;

            if (go(num + 1))
                return true;

            X[i] = 0;
        }

    return false;
}

void solve_case(int test_case)
{
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    for (int i = 0; i < N; i++)
        scanf("%d", &B[i]);

    memset(X, 0, sizeof(X));
    printf("Case #%d: ", test_case);
    go(1);

    for (int i = 0; i < N; i++)
        printf("%d%c", X[i], i < N - 1 ? ' ' : '\n');
}

int main()
{
    initialize();
    int T; scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        solve_case(tc);
        fflush(stdout);
    }

    return 0;
}
