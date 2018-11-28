#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
#include<cstdlib>
#include<queue>
#pragma comment(linker,"/STACK:1024000000,1024000000")
using namespace std;

#define N 1000005
#define L(x) x<<1
#define R(x) x<<1|1
#define M(x,y) (x + y)>>1
#define MOD 1000000007
#define MODD 1000000006
#define inf 0x7fffffff
#define llinf 0x7fffffffffffffff
#define LL long long
#define eps 1e-8

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    double c,f,x;
    int t,test = 1,n,m;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans = 0;
        double get = 2;
        double a = x/get;
        double b = c/get + x/(get + f);
        while(a >= b)
        {
    //            cout<<a<<' '<<b<<endl;
                ans += c/get;
                get += f;
                a = x/get;
                b = c/get + x/(get + f);
                if(a <= eps)
                     break;
        }
        ans += a;
        printf("Case #%d: %.7f\n",test++,ans);
    }
    return 0;
}
