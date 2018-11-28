#include <iostream>
#include <iomanip>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>
#include <bitset>


using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

void test()
{
    double c,f,x;
    scanf("%lf%lf%lf\n", &c, &f, &x);
    double res = x/2.0;
    double coockie = 0;
    double time = 0;
    double add = 2;
    rep(t,0,100000)
    {
        double here = time + (x - coockie)/add;
        res = min(res, here);
        if (coockie >= c - 1e-8)
        {
            add += f;
            coockie -=c;
            continue;
        }
        time += (c - coockie)/add;
        coockie = c;
    }
    printf("%.10lf\n", res);
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        fprintf(stderr, "Test %d...", i+1);
        printf("Case #%d: ", i+1);
        test();
        fprintf(stderr, " done!\n");
    }
}


#define prob "B-small-attempt1"


int main()
{
#ifdef _MONYURA_
    #ifdef prob
        freopen(prob".in","r",stdin);
        freopen(prob".out","w",stdout);
    #else
        freopen("test.in","r",stdin);
        freopen("test.out","w",stdout);
        time_t st=clock();
    #endif
#else
    #ifdef prob
        freopen(prob".in","r",stdin);
        freopen(prob".out","w",stdout);
    #endif
#endif
    run();
#ifdef _MONYURA_
    #ifndef prob
        printf( "\n=============\n");
        printf("Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
    #endif
#endif
    
    return 0;
}
