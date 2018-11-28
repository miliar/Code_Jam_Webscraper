#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <memory.h>
#include <ctime>
#include <cmath>

using namespace std;

int A[5][5], B[5][5];

void solve()
{
    int row1, row2;
    int ans = -1;
    scanf("%d", &row1);
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            scanf("%d", &A[i][j]);
    scanf("%d", &row2);
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            scanf("%d", &B[i][j]);
    set< int > st;
    for (int j = 0; j < 4; ++j)
        st.insert(A[row1 - 1][j]);
    for (int j = 0; j < 4; ++j)
    {
        st.insert(B[row2 - 1][j]);
        if ((int)st.size() != 4 + j + 1 && ans < 0)
            ans = B[row2 - 1][j];
    }
    switch (st.size())
    {
        case 7:
            printf("%d\n", ans);
            break;
        case 8:
            printf("Volunteer cheated!\n");
            break;
        default:
            printf("Bad magician!\n");
            break;
    }
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        printf("case #%d: ", i + 1);
        solve();
    }
    return 0;
}
