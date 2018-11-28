#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#define FI first
#define SE second
using namespace std;
const double EPS = 1e-8;
const int MAXN = 100005;
int main()
{
    freopen("/home/qitaishui/practice/retired/in.txt","r",stdin);
    freopen("/home/qitaishui/practice/retired/out.txt","w",stdout);
    int cas;
    double c,f,x;
    double rate,best,now,st;
    scanf("%d",&cas);
    for (int ca = 1;  ca <= cas; ++ca) {
        scanf("%lf%lf%lf",&c,&f,&x);
        rate = 2;
        st = 0;
        best = 1e50;
        for (int i = 0; i <= x; ++i) {
            now = st + x/rate;
            if (now + EPS < best) best = now;
            st += c/rate;
            rate += f;
        }
        printf("Case #%d: %.7f\n",ca,best);
    }
    return 0;
}
