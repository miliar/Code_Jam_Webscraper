#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <queue>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
typedef long long ll;

char s[10005];
int val[10005];

int cal(int x, int y)
{
    if (x == 1) return y;
    if (y == 1) return x;
    if (x == y) return -1;
    if (x == 2 && y == 3)   return 4;
    if (x == 2 && y == 4)   return -3;
    if (x == 3 && y == 2)   return -4;
    if (x == 3 && y == 4)   return 2;
    if (x == 4 && y == 2)   return 3;
    if (x == 4 && y == 3)   return -2;
    return 0;
}

int trans(char x)
{
    if (x == 'i')   return 2;
    if (x == 'j')   return 3;
    if (x == 'k')   return 4;
    return 0;
}

int sign(int x)
{
    return x > 0 ? 1 : -1;
}

void work()
{
    int L, X;
    scanf("%d%d", &L, &X);
    scanf("%s", s);
    for (int i = L; i < L * X; i += L) {
        for (int j = 0; j < L; ++ j) {
            s[i + j] = s[j];
        }
    }
    val[0] = trans(s[0]);
    for (int i = 1; i < L * X; ++ i) {
        val[i] = sign(val[i - 1]) * cal(abs(val[i - 1]), trans(s[i]));
    }
    if (val[L * X - 1] != -1) {
        puts("NO");
        return;
    }
    vector<int> a, b;
    for (int i = 0; i < L * X; ++ i) {
        if (val[i] == 2) {
            a.push_back(i);
        }
        if (val[i] == 4) {
            b.push_back(i);
        }
    }
    if (a.size() > 0 && b.size() && a[0] < b[b.size() - 1]) {
        puts("YES");
    }
    else {
        puts("NO");
    }
}

int main()
{
    ios :: sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    int kase = 1;
    while (T --) {
        printf("Case #%d: ", kase ++);
        work();
    }
    return 0;
}