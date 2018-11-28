#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>

#define inf 1000000007

using namespace std;

int n, c[2222];

struct node
{
    int v, mark;
};

node key[2222];

bool cmp(node a, node b)
{
    return a.v < b.v;
}

int lowbit(int x)
{
    return (x & (-x));
}

int sum(int x)
{
    int tmp = 0;
    while (x) {
        tmp += c[x];
        x -= lowbit(x);
    }
    return tmp;
}

void add(int x, int delta)
{
    while (x <= n) {
        c[x] += delta;
        x += lowbit(x);
    }
}

int a[2222];

int calcleft(int l, int r)
{
    if (l >= r) return 0;
    memset(c, 0, sizeof c);
    int cursum = 0;
    for (int i = r; i >=l; i--) {
        cursum += sum(a[i]);
        add(a[i], 1);
    }
    return cursum;
}

int calcright(int l, int r)
{
    if (l >= r) return 0;
    memset(c, 0, sizeof c);
    int cursum = 0;
    for (int i = l; i <= r; i++) {
        cursum += sum(a[i]);
        add(a[i], 1);
    }
    return cursum;
}

int main()
{
    int testcase;
    freopen("b.in", "r", stdin);
    freopen("bb.out", "w", stdout);
    scanf("%d", &testcase);
    int maxpos, maxv, minv, minpos;
    for (int test = 1; test <= testcase; test++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) {
            scanf("%d", &a[i]);
            key[i].v = a[i];
            key[i].mark = i;
        }
        sort(key + 1, key + 1 + n, cmp);
        for (int i = 1; i <= n; i++) {
            a[key[i].mark] = i;
        }
        int l, r;
        l = 1; r = n;
        int ans = 0;
        for (int rd = 1; rd <= n; rd++) {
            minv = a[l]; minpos = l;
            for (int i = l; i <= r; i++) {
                if (a[i] < minv) {
                    minv = a[i];
                    minpos = i;
                }
            }
            if (minpos - l < r - minpos) {
                int tmp = minv;
                ans += minpos - l;
                for (int i = minpos; i > l; i--)
                    a[i] = a[i - 1];
                a[l] = tmp;
                l++;
            }
            else {
                int tmp = minv;
                ans += r - minpos;
                for (int i = minpos; i < r; i++)
                    a[i] = a[i + 1];
                a[r] = tmp;
                r--;
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
