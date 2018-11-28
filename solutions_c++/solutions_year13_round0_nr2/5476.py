#include<iostream>
#include<cstdio>
#include<string>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<climits>
using namespace std; 
#define rep(i,n) for(i=0; i<(n); i++)
#define reph(i,n,m) for(i=(n); i<=(m); i++)//正循环的
#define repd(i,n,m) for(i=(n); i>=(m); i--) //负循环的 
#define fab(a) (a)>0?(a):0-(a)
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define ll __int64
#define arc(a) (a)*(a)
#define inf 10000000   //最大值的
#define exp 0.0000001     //浮点型的
#define N   105  //记录开的数组
int map[105][105];
int main()
{
    int T,n,m,i,j,k;
    scanf("%d",&T);
    int ror;
    reph(ror,1,T)
    {
        scanf("%d%d",&n,&m);
        reph(i,1,n)
        {
            reph(j,1,m)
             scanf("%d",&map[i][j]);
        }
        int sign=0;
        reph(i,1,n)
        {
            reph(j,1,m)
            {
                int a=0,b=0;;
                 reph(k,1,m)
                   if(map[i][k]>map[i][j])
                   {
                    a=1;
                    break;
                }
                reph(k,1,n)
                  if(map[k][j]>map[i][j])
                  {
                   b=1;
                   break;
                } 
                if(a==1 && b==1)
                 {
                        sign=1;
                        break;
                    }
            }
            if(sign==1)
                  break;
        }
        printf("Case #%d: ",ror);
        if(sign==0)
         printf("YES\n");
         else
         printf("NO\n");
    }
    return 0;
} 
