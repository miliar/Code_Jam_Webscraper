/*************************************************************************
	> File Name: b.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2015年04月11日 星期六 14时39分08秒
 ************************************************************************/

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cassert>
// #pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
#define LL long long
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define x first
#define y second
#define MAXN 1005
template <typename T> inline T Max(T a, T b) {return a>b?a:b;}
template <typename T> inline T Min(T a, T b) {return a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
int T, Cas = 1;

int D, P[MAXN], ans;

int gao(int minValue) {
    int tmp[MAXN] = {};
    int ans = minValue;
    for (int i = 1; i <= D; i ++) {
        ans = ans + P[i] / minValue - (P[i] % minValue == 0);
    }
    return ans;
}

void work() {
    printf("Case #%d: ", Cas ++);
    scanf("%d", &D);
    for (int i = 1; i <= D; i ++) {
        scanf("%d", &P[i]);
    }
    sort(P + 1, P + 1 + D);
    int len = P[D];
    ans = P[D];
    for (int i = 1; i <= len; i ++) {
        ans = Min(ans, gao(i));
    }
    cout << ans << endl;
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
