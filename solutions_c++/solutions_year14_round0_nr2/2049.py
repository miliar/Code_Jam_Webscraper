#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <vector>

#define FOR(i,a,b) for(int i=a,_b=b;i<=_b;i++)
#define FO(i,a,b) for(int i=a,_b=b;i<_b;i++)
#define FORD(i,a,b) for(int i=a,_b=b;i>=_b;i--)
#define FOD(i,a,b) for(int i=a,_b=b;i>_b;i--)

#define LL long long
#define pi 2*acos(0.0)
using namespace std;

double c, f, x;

void input(){
    scanf("%lf%lf%lf", &c, &f, &x);
}

void process(){
    double cur = 2.0;
    double ans = x/cur;
    double addedTime = 0;
    FOR (i, 1, 1e6){
        addedTime += c/cur;
        if (addedTime > x/2.0) break;
        cur += f;
        ans = min(ans, addedTime + x/cur);
    }
    printf("%0.7lf\n", ans);
}

int main(){
    //freopen("test.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    FOR (i, 1, test){
        printf("Case #%d: ", i);
        input();
        process();
    }
    return 0;
}

