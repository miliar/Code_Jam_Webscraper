#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

double calc(double C,double F,double X,double rate)
{
    if(X/rate < (C/rate+ X/(rate+F)))
        return X/rate;
    else
        return (C/rate+calc(C,F,X,rate+F));
}
int main()
{   freopen("B-small-attempt0.in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    int i;
    double C,F,X;
    double ans;
    for(i=1;i<T+1;i++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        ans=calc(C,F,X,2.00);
        printf("Case #%d: %.7f\n",i,ans);

    }
}
