
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include "iostream"
#include "cstring"
#include "algorithm"
#include "cmath"
#include "cstdio"
#include "sstream"
#include "queue"
#include "vector"
#include <math.h>
#include "string"
#include "stack"
#include "cstdlib"
#include "deque"
#include "fstream"
#include "map"
#include "set"
#define lson(x) (x<<1)
#define rson(x) (x<<1|1)
#define MID(x,y) ((x+y)>>1)
#define FR (freopen("in.txt","r",stdin))
#define clr(a,b) memset(a,b,sizeof(a))
#define lowbit(t) (t&-t)
#define mkp make_pair
using namespace std;
typedef long long LL;
const int MAXN = 10000+10;
const int inf = 522133279;
const int mod = 1000000007;
const double PI = 3.14159265358979323846;

double c,f,x;
int t;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ooo.txt","w",stdout);
    scanf("%d",&t);
    for(int ka =1 ; ka <= t; ka++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double curget=2;
        double time=0;

        while(x/curget > c/curget+x/(curget+f))
        {
            time += c/curget;
            curget+=f;
        }
        time += x/curget;

        printf("Case #%d: %.7lf\n",ka,time);
    }
    return 0;
}
