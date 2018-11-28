#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

#define PB push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define DWN(i,h,l) for(int i=(h);i>=(l);--i)
#define CLR(arr) memset(arr,0,sizeof(arr))
#define MAX3(a,b,c) max(a,max(b,c))
#define MAX4(a,b,c,d) max(max(a,b),max(c,d))
#define MIN3(a,b,c) min(a,min(b,c))
#define MIN4(a,b,c,d) min(min(a,b),min(c,d))
#define MST(arr,val) memset(arr,val,sizeof(arr))
#define PI acos(-1.0)
#define oo 1000000000
#define loo 1000000000000000000LL
#define eps 1e-8

typedef long long ll;

int dx[]={0,0,-1,1};
int dy[]={-1,1,0,0};

int main()
{
    freopen("in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cs = 0,n,k;
    double c,f,x,total,temp,speed;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        total = 0;
        temp = f * x - 2 * c - f * c;
        if(temp > 0)
        {
            n = (int)(temp/f/c);
            if(fabs(f*c*(double)n-temp) < eps) ;
            else n++;
        }
        else
        n = 0;
        speed = 2;
        REP(i,n)
        {
            total += c / speed;
            speed += f;
        }
        total += x / speed;
        printf("Case #%d: %.7lf\n",++cs,total);
    }
    return 0;
}
