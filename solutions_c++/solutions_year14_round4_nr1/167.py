

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
typedef vector<int> vi;

typedef pair<int, string> pis;

int  fullTest(vi arr, int x)
{
    vi perm;
    rep(i, 0, arr.size())
    perm.push_back(i);
    int res = arr.size();
    do
    {
        int cr = arr.size();
        for (int i = 0; i < arr.size() - 1; i += 2)
        {
            if (arr[perm[i]] + arr[perm[i+1]] <= x)
            cr--;
        }
        res = min(res, cr);
    }
    while(next_permutation(perm.begin(), perm.end()));
    return res;
}

void test(int tIndex)
{
    printf("Case #%d: ", tIndex);
    vector<int> arr;
    int n, x;
    scanf("%d%d", &n, &x);
    rep(i, 0, n)
    {
        int cn;
        scanf("%d", &cn);
        
        arr.push_back(cn);
    }
    
//    int ta = fullTest(arr, x);
    
    sort(all(arr));
    
    int fs = 0, ed = arr.size() - 1;
    int res = 0;
    while (fs <= ed)
    {
        if (arr[fs] + arr[ed] <= x)
        {
            res++;
            fs++;
            ed--;
        }
        else
        {
            res++;
            ed--;
        }
    }
    
//    if (fs == ed)
//    res++;
    printf("%d\n", res);
}

void run()
{
	int T, t;
	scanf("%d", &T);
	for(t = 0; t < T; ++t)
	{
		test(t + 1);
	}
}

//#define prob "settling"


int main()
{
#ifdef LOCAL_DEBUG
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    time_t st=clock();
#else
#ifdef prob
    freopen(prob".in","r",stdin);
    freopen(prob".out","w",stdout);
#endif
#endif
    run();
#ifdef LOCAL_DEBUG
    fprintf(stderr,  "\n=============\n");
    fprintf(stderr, "Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif
    
    return 0;
}