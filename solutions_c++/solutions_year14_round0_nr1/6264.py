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

int a[4][5],b[4][5];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,r1,r2,cs = 0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&r1);
        REP(i,4)
        REP(j,4)
            scanf("%d",&a[i][j]);
        scanf("%d",&r2);
        REP(i,4)
        REP(j,4)
            scanf("%d",&b[i][j]);
        int total = 0;
        int ans;
        r1 -- ;
        r2 -- ;
        REP(i,4)
        {
            REP(j,4)
            {
                if(a[r1][i] == b[r2][j])
                total++,ans = i;
            }
        }
        printf("Case #%d: ",++cs);
        if(total == 1)
        printf("%d\n",a[r1][ans]);
        else if(total)
        puts("Bad magician!");
        else
        puts("Volunteer cheated!");
    }
    return 0;
}
