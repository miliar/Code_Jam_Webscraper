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
typedef pair<double, int> pdi;

const int SZ = 1010;

void test()
{
    int A[1010], S[1010];
    int n;
    cin>>n;
    rep(i,0,n)
    {
        scanf("%d", A+i);
        S[i] = A[i];
    }
    sort(S,S+n);
    int res = 0;
    rep(i,0,n)
    {
        int pos = 0;
        rep(j,0,n)
        if (A[j] == S[i])
            pos = j;
        int a = 0, b = 0;
        rep(j,0,n)
        if (A[j] > S[i])
        {
            if (j < pos)
                ++a;
            else
                ++b;
        }
        res += min(a,b);
    }
    cout<<res<<endl;
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        cerr<<"test "<<i+1<<endl;
        printf("Case #%d: ", i+1);
        test();
    }
}


#define prob "B-large(2)"


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
