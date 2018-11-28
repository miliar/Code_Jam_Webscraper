#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <list>
using namespace std;
double C, F, X, ans;

int main()
{
    int test, times=1;
    scanf("%d", &test);
    while(test--){
        double rate=2.0, ans=0.0, now=0.0, farm=0.0, oldT=0.0, newT=0.0;
        scanf("%lf %lf %lf", &C, &F, &X);

        oldT = X/rate, farm = C/rate, newT = farm + X/(rate+F);
        while(newT<oldT){
            ans+=farm;
            rate+=F;
            oldT = X/rate, farm = C/rate, newT = farm + X/(rate+F);
        }
        ans+=oldT;
        printf("Case #%d: %.7f\n", times++, ans);
    }
    return 0;
}
