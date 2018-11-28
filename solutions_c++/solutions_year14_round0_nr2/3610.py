#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<cmath>
#include<queue>
#include<set>
using namespace std;
#define N 100000
#define LL long long
#define INF 0xfffffff
const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = ~0u>>2;
int a[5][5];
int b[5][5];
bool f[20];
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int t;
    double c,f,x;
    cin>>t;
    int kk=0;
    while(t--)
    {
        cin>>c>>f>>x;
        double o = 2.0;
        double ans = 0;
        while(1)
        {
           double s = c/o;
           double s1 = x/(o+f)+s;
           double s2 = x/o;
           if(s2<s1)
           {
               ans+=s2;
               break;
           }
           o+=f;
           ans+=s;
        }
        printf("Case #%d: %.7f\n",++kk,ans);
    }
    return 0;
}
