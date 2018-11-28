#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
using namespace std;
typedef long long LL;
int ca;
#define N 5005

double C , F , X;
void work()
{
    double ans = 1e60;
    double t = 0 , d = 2 , pre = 1e60 , now;
    cin >> C >> F >> X;

    while (1) {
        //printf("%f\n" , t + X / d);
        now = t + X / d;
        if (now > pre) break;
        ans = min(ans , now) , pre = now;
        t += C / d , d += F;
    }
    printf("Case #%d: %.10f\n" , ++ ca , ans);
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
