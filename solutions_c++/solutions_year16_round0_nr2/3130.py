/*************************************************************************
	> File Name: RevengeOfThePancakes.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2016年04月09日 星期六 15时34分57秒
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
#define x first
#define y second
template <typename T> inline void checkMax(T &a, T b) {a = a>b?a:b;}
template <typename T> inline void checkMin(T &a, T b) {a = a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
const double eps = 1e-8;
int T, Cas = 1, n;

char str[105];

void work() {
    printf("Case #%d: ", Cas ++);
    scanf("%s", str + 1);
    n = strlen(str + 1);
    int want = 1, ans = 0;
    for (int i = n; i >= 1; i --) {
        if (str[i] == '-') {
            if (want == 1) {
                ans ++;
                want = 0;
            }
        } else {
            if (want == 0) {
                ans ++;
                want = 1;
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
