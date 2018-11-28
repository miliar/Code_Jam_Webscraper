#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#define zero(x) (((x)>0?(x):-(x))<eps)
#define mem(a,b) memset((a),(b),sizeof((a)))
#define lld long long
#define INF 0x3f3f3f3f
#define eps 1e-6
#define num_char 26
#define hash(x) ((x)-'a')
#define N 100009

using namespace std;

double c, f, x;

int MAIN() {
    scanf("%lf%lf%lf", &c, &f, &x);
    double ans = x / 2;
    double t = 0;
    double p = 2;
    for(int i = 1; i <= 100000; i++) {
        t += c / p;
        p += f;
        ans = min(ans, t + x / p);
    }
    printf("%.7lf\n", ans);
    return 0;
}


int main() {
#ifdef LOCAL_TEST
    freopen("F:/ACMData.txt","r",stdin);
    freopen("F:/out.txt","w",stdout);
#endif
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    while(cases--) {
        printf("Case #%d: ", cc++);
        MAIN();
    }
    return 0;
}

