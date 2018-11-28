#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<queue>
#include<vector>
#include<list>
#include<map>
#include<string>
#include<deque>
#include<set>

using namespace std;

#define LS (v<<1)
#define RS (v<<1|1)
#define MID (l+r>>1)
#define INF 0x7fffffff
#define INFL 0x7fffffffffffffffll
#define maxn 0

int egcd(int a,int b,int &x,int &y)
{
    if(b==0)
    {
        x=1,y=0;
        return a;
    }
    int c=egcd(b,a%b,x,y);
    int d=x;
    x=y;
    y=d-a/b*x;
    return c;
}
int gcd(int a,int b){return b?gcd(b,a%b):a;}
int cb[1][1];
void Combination(int len,int mod)
{
    cb[0][0]=1;
    for(int i=1;i<=len;i++)
    {
        cb[i][0]=1;
        for(int j=1;j<=len;j++)
        {
            cb[i][j]=(cb[i-1][j-1]+cb[i-1][j])%mod;
        }
    }
}

int n,m;
__int64 e[10001000],a,b;
int tol;


void INIT()
{
    int j,len,len2;
    __int64 i,tmp;
    char num[20];
    tol=0;
    for(i=1;i<=10000000;i++)
    {
        tmp=i;
        len=0;
        while(tmp)
        {
            num[len++]=tmp%10+'0';
            tmp/=10;
        }
        len2=len/2;
        for(j=0;j<len2;j++)
        {
            if(num[j]!=num[len-j-1]) break;
        }
        if(j<len2) continue;
        tmp=i*i;
        len=0;
        while(tmp)
        {
            num[len++]=tmp%10+'0';
            tmp/=10;
        }
        len2=len/2;
        for(j=0;j<len2;j++)
        {
            if(num[j]!=num[len-j-1]) break;
        }
        if(j<len2) continue;
        e[tol]=i*i;
        tol++;
    }
   // for(i=1;i<=tol;i++) cout<<e[i]<<endl;
}

int result(__int64 x)
{
    int l,r,mid;
    l=0,r=tol-1;
    while(l<=r)
    {
        mid=MID;
        if(x<e[mid])
        {
            r=mid-1;
        }
        else
        {
            l=mid+1;
        }
    }
    return r;
}

int main()
{
 //   freopen("C-large-1.in","r",stdin);
 //   freopen("C-large-1.out","w",stdout);
    int l,r;
    int cas=1,t;
    INIT();
    scanf("%d",&t);
    while(t--)
    {
        scanf("%I64d%I64d",&a,&b);
        printf("Case #%d: %d\n",cas++,result(b)-result(a-1));
    }
    return 0;
}
