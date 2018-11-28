#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAXN = 5;
bool ok[MAXN][MAXN][MAXN];

void pre() {
    ok[1][1][1] = true;

    ok[1][2][1] = true;
    ok[1][2][2] = true;

    ok[1][3][1] = true;

    ok[1][4][1] = true;
    ok[1][4][2] = true;

    ok[2][2][1] = true;
    ok[2][2][2] = true;

    ok[2][3][1] = true;
    ok[2][3][2] = true;
    ok[2][3][3] = true;

    ok[2][4][1] = true;
    ok[2][4][2] = true;

    ok[3][3][1] = true;
    ok[3][3][3] = true;

    ok[3][4][1] = true;
    ok[3][4][2] = true;
    ok[3][4][3] = true;
    ok[3][4][4] = true;

    ok[4][4][1] = true;
    ok[4][4][2] = true;
    ok[4][4][4] = true;
}

int main() {
    pre();

    int tc;
    scanf("%d", &tc);
    for(int ii=1;ii<=tc;++ii) {
        int X, R, C;
        scanf("%d %d %d", &X, &R, &C);

        printf("Case #%d: ", ii);
        if(ok[min(R, C)][max(R, C)][X])
            printf("GABRIEL");
        else
            printf("RICHARD");
        printf("\n");
    }
    return 0;
}
