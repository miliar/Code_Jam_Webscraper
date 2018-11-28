
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

int t;
int g[5][5],g2[5][5];
int n,m;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ooo.txt","w",stdout);
    scanf("%d",&t);
    for(int ka =1 ; ka <= t; ka++)
    {
        scanf("%d",&n);
        for(int i = 1 ; i <= 4 ; i++)
            for(int j = 1 ; j <= 4;  j++)
                scanf("%d",&g[i][j]);
        scanf("%d",&m);
        for(int i = 1 ; i <= 4 ; i++)
            for(int j = 1 ; j <= 4;  j++)
                scanf("%d",&g2[i][j]);

        int cnt=0,pos;
        for(int i =1 ; i <= 4 ; i++)
            for(int j = 1 ; j <= 4 ; j++)
            {
                if(g[n][i] == g2[m][j])
                {
                    cnt++;
                    pos=g[n][i];
                }
            }

        printf("Case #%d: ",ka);
        if(cnt==1)
            printf("%d\n",pos);
        else if(cnt > 1)
            printf("Bad magician!\n");
        else
            printf("Volunteer cheated!\n");

    }
    return 0;
}
