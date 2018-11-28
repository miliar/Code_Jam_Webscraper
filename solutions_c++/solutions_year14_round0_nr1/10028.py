//#include<CSpreadSheet.h>

#include<iostream>
#include<cmath>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<string>
#include<string.h>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<queue>
#include<ctime>
#include<bitset>
#define eps 1e-6
#define INF 0x3f3f3f3f
#define PI acos(-1.0)
#define ll __int64
#define LL long long
#define lson l,m,(rt<<1)
#define rson m+1,r,(rt<<1)|1
#define M 1000000007
//#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;

#define Maxn 12

int save1[Maxn][Maxn];
int save2[Maxn][Maxn];

int main()
{
   freopen("A-small-attempt0.in","r",stdin);
   freopen("A-small-attempt0.out","w",stdout);
   int t;

   scanf("%d",&t);
   for(int ca=1;ca<=t;ca++)
   {
       int r1,r2;

       scanf("%d",&r1);
       for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&save1[i][j]);
       scanf("%d",&r2);
       for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&save2[i][j]);

       int ans=0,res;

       for(int i=1;i<=4;i++)
       {
           for(int j=1;j<=4;j++)
           {
               if(save1[r1][i]==save2[r2][j])
               {
                   ans++;
                   res=save1[r1][i];
               }
           }
       }
       if(!ans)
           printf("Case #%d: Volunteer cheated!\n",ca);
       else if(ans==1)
            printf("Case #%d: %d\n",ca,res);
       else
            printf("Case #%d: Bad magician!\n",ca);
   }
   return 0;
}


