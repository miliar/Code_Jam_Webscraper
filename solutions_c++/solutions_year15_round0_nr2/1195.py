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
#include <cassert>


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
typedef pair<double, int> pdi;
typedef pair<double, double> pdd;

void test()
{
    int n;
    cin>>n;
    int A[1010];
    rep(i,0,n)
        scanf("%d",A + i);
    int res = *max_element(A, A + n);
    rep(i, 1, res + 1)
    {
        int here = i;
        rep(j,0,n)
            here += max(0, (A[j] + i - 1)/i - 1);
        res = min(res, here);
    }
    cout<<res<<endl;
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        printf("Case #%d: ", i + 1);
        test();
    }
}

#define prob "B-large(3)"



int main()
{
#ifdef _MONYURA_
    #ifdef prob
        freopen("../" prob ".in","r",stdin);
        freopen("../" prob ".out","w",stdout);
    #else
        freopen("../test.in","r",stdin);
        freopen("../test.out","w",stdout);
        time_t st=clock();
    #endif
#else
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