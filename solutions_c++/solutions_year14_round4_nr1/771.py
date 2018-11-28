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

void test()
{
    int n,x;
    cin>>n>>x;
    int A[10100];
    rep(i,0,n)
        scanf("%d",A+i);
    sort(A,A+n);
    multiset<int> ms(A,A+n);
    int res = n;
    while(ms.size()>0)
    {
        multiset<int>::iterator iter = ms.begin(), next;
        int val = *iter;
        ms.erase(iter);
        next = ms.upper_bound(x - val);
        if (next != ms.begin())
        {
            --next;
            --res;
            ms.erase(next);
        }
    }
    cout<<res<<endl;
    
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        cerr<<i+1<<endl;
        printf("Case #%d: ", i+1);
        test();
    }
}


#define prob "A-large(1)"


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
