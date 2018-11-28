/*************************************************************************
	> File Name: c.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2015年04月11日 星期六 15时27分35秒
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
#define MAXN 10005
template <typename T> inline T Max(T a, T b) {return a>b?a:b;}
template <typename T> inline T Min(T a, T b) {return a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
int T, Cas = 1;
int L, K;
char str[MAXN];

bool small_ok1[MAXN], small_ok2[MAXN];

int mat[][4] = {
    {1, 2, 3, 4},
    {2, -1, 4, -3},
    {3, -4, -1, 2},
    {4, 3, -2, -1}
};

struct Node {
    int value;

    Node() {}

    Node(char c) {
        if (c == 'i') {
            value = 2;
        } else if (c == 'j') {
            value = 3;
        } else {
            value = 4;
        }
    }

    Node(int d) : value (d) {}

    Node operator * (const Node &next) {
        int a = abs(value), b = abs(next.value), o = value > 0 ? 1 : -1, oo = next.value > 0 ? 1 : -1;
        int c = mat[a - 1][b - 1], ooo = (c > 0 ? 1 : -1) * o * oo;
        return Node(ooo * abs(c));
    }
};

void small_task() {
    for (int i = 2; i <= K; i ++) {
        for (int j = 1; j <= L; j ++) {
            str[(i - 1) * L + j] = str[j];
        }
    }
    Node a = Node(str[1]);
    memset(small_ok1, 0, sizeof(small_ok1));
    memset(small_ok2, 0, sizeof(small_ok2));
    if (a.value == 2) {
        small_ok1[1] = true;
    }
    for (int i = 2; i <= L * K; i ++) {
        a = a * Node(str[i]);
        small_ok1[i] = small_ok1[i - 1];
        if (a.value == 2) {
            small_ok1[i] = true;
        }
    }
    a = Node(str[L * K]);
    if (a.value == 4) {
        small_ok2[L * K] = true;
    }
    for (int i = L * K - 1; i >= 1; i --) {
        a = Node(str[i]) * a;
        if (a.value == 4) {
            small_ok2[i] = true;
        }
    }
    a = Node(str[1]);
    for (int i = 2; i <= L * K; i ++) {
        a = a * Node(str[i]);
        if (a.value == 4) {
            if (small_ok1[i - 1] && small_ok2[i + 1]) {
                printf("YES\n"); return ;
            } 
        }
    }
    printf("NO\n"); return ;
}

void work() {
    printf("Case #%d: ", Cas ++);
    scanf("%d %d", &L, &K);
    scanf("%s", str + 1);
    small_task();
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
