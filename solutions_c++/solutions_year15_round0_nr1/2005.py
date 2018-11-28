#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);
#define AB(a) ((a)<(0) ? (-(a)) : (a))
#define EQ(a,b) ( (fabs((a)-(b))<EPS) ? (1) : (0))



typedef long long LL;
//typedef __int64 LL;


char in[5010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;

    int T,n;
    scanf("%d",&T);
    for(int cs=1;cs<=T;cs++)
    {
       scanf("%d %s",&n,in);



       int last=0;
       int ans=0;

       for(i=0;i<=n;i++)
       {
         if(in[i]>'0')
         {
           if(last<i)
           {
             int add=(i-last);
             ans+=add;
             last+=add;
           }
         }
         last+=in[i]-'0';
       }
       printf("Case #%d: %d\n",cs,ans);
    }



    return 0;
}
