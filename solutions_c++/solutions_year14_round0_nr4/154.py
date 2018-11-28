#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
typedef long long LL;
int ca;
#define N 1005

int n , a[N] , b[N];
set<int> hash;
int ans1 , ans2;
void work()
{
    printf("Case #%d: " , ++ ca);
    int i , j , k ; double x;
    scanf("%d",&n);
    for (i = 0 ; i < n ; ++ i) {
        scanf("%lf",&x);
        x *= 1e5;
        a[i] = x + 0.2;
    }
    for (i = 0 ; i < n ; ++ i) {
        scanf("%lf",&x);
        x *= 1e5;
        b[i] = x + 0.2;
    }
    sort(a , a + n);
    sort(b , b + n);
    //for (i = 0 ; i < n ; ++ i) {
    //    printf("%d %d\n" , a[i] , b[i]);
    //}
    int cnt = 0;
    for (i = 0 ; i < n ; ++ i) {
        hash.insert(b[i]);
    }
    for (i = 0 ; i < n ; ++ i) {
        set<int>::iterator it = hash.upper_bound(a[i]);
        if (it == hash.end())
            it = hash.begin();
        if (a[i] > *it)
            ++ cnt;
        hash.erase(it);
    }
    ans2 = cnt , ans1 = 0;
    for (i = 0 , j = 0 , k = n - 1; i < n ; ++ i) {
        if (a[i] < b[j]) {
            -- k;
        } else {
            ++ ans1;
            ++ j;
        }
    }

    printf("%d %d\n" , ans1 , ans2);
}

int main (){
    freopen("1.txt" , "r" , stdin);
    freopen("2.txt" , "w" , stdout);

    int T;
    scanf("%d",&T);
    while (T --) {
        work();
    }
    return 0;
}
