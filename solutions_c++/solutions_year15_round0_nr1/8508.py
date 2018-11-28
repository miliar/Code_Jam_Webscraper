#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
/**zhaoruifeng.kopyh.2015*/
#define INF 0x3f3f3f3f
#define PI 3.141592653589793
#define LL long long
#define mod 100000000
#define eps 1e-6
#define N 1000010
#define PRIME 999983
#define lson rt<<1,l,(l+r)>>1
#define rson rt<<1|1,(l+r)>>1+1,r
using namespace std;

int n,m;
int flag,sum,ave,ans,res;
int a[101],b[101];
//int g[101][101];
char s[101];
struct node
{
    int x,y;
    int r;
};

int dir[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
//int dir[8][2]={{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
int month[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int dirs(char c){switch(c){case 'N': return 0; case 'W': return 1; case 'S': return 2; default: return 3;}}
//bool Inside(int x,int y)
//{   return x>=0&&x<n&&y>=0&&y<m;  }
//bool compare(node x,node y)//ÉýÐò
//{
//	if(x.r>y.r)
//		return false;
//	return true;
//}return 1;

int main()
{
    int i,j,k,t;
    #ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
      freopen("out.out","w",stdout);
    #endif
//    while(scanf("%d",&s)!=EOF)
    scanf("%d",&k);
    t=0;
    while(k--)
    {
        t++;
        scanf("%d%s",&n,s);
//        printf("%d %s\n",n,s);
        res=0;
        sum=s[0]-'0';
        for(i=1;i<=n;i++)
        {
//            printf("%d %d %d %d\n",i,sum,res,s[i]-'0');
            if(s[i]=='0')continue;
            if(i>sum)
            {
                res+=(i-sum);
                sum=i+s[i]-'0';
            }
            else
            {
                sum+=s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",t,res);
    }
    return 0;
}







