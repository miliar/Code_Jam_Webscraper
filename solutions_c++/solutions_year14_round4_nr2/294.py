#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;
typedef long long LL;
#define N 1005
int ca;
int n , a[N];
int d[N];
int c[N];
int A[N] , b[N] , p[N];
int get(bool f) {
    memset(c , 0 , sizeof(c));
    int sum = 0 , i , j;
    for (i = 0 ; i < n; ++ i) {
        int x = A[i];
        if (f)
            ++ x;
        else
            x = n - x;
        for (j = x ; j > 0 ; j -= j & -j)
            sum += c[j];
        for (j = x ; j <= n ; j += j & -j)
            ++ c[j];
    }
    return sum;
}

void work() {
    printf("Case #%d: " , ++ ca);
    int i , j , x , y;
    scanf("%d",&n);
    for (i = 0 ; i < n ; ++ i) {
        scanf("%d",&a[i]);
        d[i] = a[i];
    }
    sort(d , d + n);
    for (i = 0 ; i < n ; ++ i) {
        a[i] = lower_bound(d , d + n , a[i]) - d;
        p[a[i]] = i;
        if (a[i] + 1 == n)
            y = i;
    }
    int l = 0 , r = 0 , ans = 0;
    for (i = 0 ; i < n ; ++ i) {
        int pos;
        for (j = 0 ; j < n ; ++ j)
            if (a[j] == i)
                pos = j;
        if (pos - l <= n - r - 1 - pos) {
            while (pos != l) {
                swap(a[pos] , a[pos - 1]);
                -- pos , ++ ans;
            }
            ++ l;
        } else {
            while (pos != n - r - 1) {
                swap(a[pos] , a[pos + 1]);
                ++ pos , ++ ans;
            }
            ++ r;
        }
    }
    /*
    int ans = 1 << 30;
    for (i = 0 ; i < 1 << n - 1 ; ++ i) {
        int m = 0;
        for (j = 0 ; j < n - 1 ; ++ j) {
            if (i >> j & 1)
                b[m ++] = j;
        }
        b[m ++] = n - 1;
        for (j = n - 2 ; j >= 0 ; -- j) {
            if (~i >> j & 1)
                b[m ++] = j;
        }
        for (j = 0 ; j < n ; ++ j)
            A[j] = p[b[j]];
        ans = min(ans , get(1));
    }*/
    printf("%d\n" , ans);
}

int main()
{
    freopen("~input.txt" , "r" , stdin);
    freopen("~output.txt" , "w" , stdout);
    int _; scanf("%d",&_); while (_ --)
        work();
    return 0;
}
