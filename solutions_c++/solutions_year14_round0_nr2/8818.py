#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define mp make_pair
#define xx first
#define yy second
#define pb push_back
using namespace std;
double c,f,x,rate,time,z;
int t;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int CASE=0;
    while(t--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);z=x;
        rate=2.0;time=0.0;
        while(x/rate>(c/rate+x/(rate+f)))
        {
            time+=c/rate;
            //x+=c;
            rate+=f;
        }
        time+=z/rate;
        printf("Case #%d: %.7lf\n",++CASE,time);
    }
    return 0;
}

