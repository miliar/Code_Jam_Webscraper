/*************************************************************************
	> File Name: fractiles.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2016年04月09日 星期六 21时04分16秒
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
int T, Cas = 1;

LL K, C, S;

void small_task() {
    for (int i = 1; i <= S; i ++) {
        printf("%d%c", i, " \n"[i == S]);
    }
}

void work() {
    scanf("%lld %lld %lld", &K, &C, &S);
    printf("Case #%d: ", Cas ++);
    small_task();
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
