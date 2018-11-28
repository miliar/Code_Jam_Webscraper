#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

int E, R, N, v[10];
int maxv;
void cal(int lev, int gain, int en) {
    //cout << lev << ' '  << gain << ' ' << en << endl;
    if (lev == N) {
        maxv = max(maxv, gain);
        return ;
    }
    for (int e = 0; e <= E; e++) {
        if (e > en) {
            break;
        }
        cal(lev + 1, gain + e * v[lev], min(en - e + R, E));
    }
}
int main()
{
    int T;
    scanf("%d", &T);
    int casenum = 1;
    while (T--) {
        printf("Case #%d: ", casenum++);
        scanf("%d%d%d", &E, &R, &N);
        maxv = 0;
        for (int i = 0; i < N; i++) {
            scanf("%d", &v[i]);
        }
        cal(0, 0, E);
        printf("%d\n", maxv);
    }
	return 0;
}
