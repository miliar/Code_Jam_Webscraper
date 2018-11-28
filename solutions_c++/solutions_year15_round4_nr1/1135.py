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

void test(int testInd)
{
    int n,m;
    cin>>n>>m;
    char A[101][101];
    rep(i,0,n)
        scanf("%s",A[i]);
    string arr = ">v<^.";
    int dx[] = {0,1,0,-1,0};
    int dy[] = {1,0,-1,0,0};
    int res = 0;
    rep(i,0,n)
    rep(j,0,m)
    if (A[i][j] != '.')
    {
        int pos = arr.find(A[i][j]);
        int x = i + dx[pos];
        int y = j + dy[pos];
        bool meet = false;
        while (x>=0 && x<n && y>=0 && y<m)
        {
            if (A[x][y] != '.')
            {
                meet = true;
                break;
            }
            x += dx[pos];
            y += dy[pos];
        }
        res += !meet;
        if (!meet)
        {
            rep(dir,0,4)
            {
                int x = i + dx[dir];
                int y = j + dy[dir];
                while (x>=0 && x<n && y>=0 && y<m)
                {
                    if (A[x][y] != '.')
                    {
                        meet = true;
                        break;
                    }
                    x += dx[dir];
                    y += dy[dir];
                }
            }
            if (!meet)
            {
                puts("IMPOSSIBLE");
                return;
            }
        }
    }
    printf("%d\n", res);
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        printf("Case #%d: ", i+1);
        test(i);
    }
}

#define prob "A-large"



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