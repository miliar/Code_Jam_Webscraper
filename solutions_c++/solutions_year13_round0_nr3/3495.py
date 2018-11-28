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
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;
const int inf = int(1e9)+7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))


bool isHuiwen(int x) {
    int tmp = x;
    int y = 0;
    while (tmp) {
        y = y*10 + tmp%10;
        tmp /= 10;
    }
    return (x == y);
}
int main() {
    int caseNum;
    scanf("%d", &caseNum);
    FOR(rp,caseNum) {
        int a, b;
        scanf("%d%d", &a, &b);
        int ans = 0;
        for (int i = 1; i <= 100; i++) if (isHuiwen(i)) {
            int x = i*i;
            if (x >= a && x <= b && isHuiwen(x)) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", rp+1, ans);
    }
    return 0;
}

