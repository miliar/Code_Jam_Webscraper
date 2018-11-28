/*************************************************************************
	> File Name: a.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2015年04月11日 星期六 12时59分41秒
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
int T, Cas = 1, N;
char str[MAXN];

void work() {
    printf("Case #%d: ", Cas ++);
    scanf("%d %s", &N, str);
    int pre = 0, ans = 0;
    for (int i = 0; i <= N; i ++) {
        int num = str[i] - '0';
        if (i == 0) {
            pre = num;
        } else {
            if (pre < i) {
                ans = ans + i - pre;
                pre = pre + i - pre + num;
            } else {
                pre = pre + num;
            }
        }
    }
    printf("%d\n", ans);
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
