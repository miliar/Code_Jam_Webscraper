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
#define N 2
int ca;
LL a , b;
map<LL , int> p;

void work()
{
    int i , j ;
    printf("Case #%d: " , ++ca);
    scanf("%lld/%lld" , &a , &b);
    LL d = __gcd(a , b);
    a /= d , b /= d;
    if (!p.count(b)) {
        puts("impossible");
        return;
    }
    j = p[b] , i = 0;
    while (a > 1) {
        a >>= 1;
        ++ i;
    }
    printf("%d\n" , j - i);
}

int main()
{
    freopen("1.txt" , "r" , stdin);
    freopen("2.txt" , "w" , stdout);

    for (int i = 0 ; i < 60 ; ++ i)
        p[1LL << i] = i;
    int _; scanf("%d", &_); while (_ --)
        work();
    return 0;
}
