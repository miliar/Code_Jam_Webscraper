/*************************************************************************
	> File Name: counting_sheep.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2016年04月09日 星期六 14时48分54秒
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

int N;

set<int> myset;

void del(int n) {
    while (n) {
        myset.erase(n % 10);
        n /= 10;
    }
}

void work() {
    printf("Case #%d: ", Cas ++);
    scanf("%d", &N);
    myset.clear();
    for (int i = 0; i <= 9; i ++) {
        myset.insert(i);
    }
    if (N == 0) {
        printf("INSOMNIA\n");
    } else {
        for (int i = 1; i <= 100; i ++) {
            del(N * i);
            if (myset.size() == 0) {
                printf("%d\n", N * i);
                return ;
            }
        }
        printf("ok\n");
    }
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
