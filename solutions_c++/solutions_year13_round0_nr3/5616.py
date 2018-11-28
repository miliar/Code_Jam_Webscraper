/** @author Ujjwal Prakash aka codeDREAMER ,NIT Jamshedpur */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<malloc.h>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<deque>
#include<list>
#include<utility>
#include<stack>
#define get getchar//_unlocked
#include<cassert>
#define LL long long
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define INF 1000000009
#define INT_MIN -1000000009
#define MOD 1000000007
using namespace std;
LL n,m;
inline LL inp()
{
    LL n=0,s=1;
    char p=get();
    if(p=='-')
    s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
    p=get();
    if(p=='-')
    s=-1,p=get();
    while(p>='0'&&p<='9')
    {
    n = (n<< 3) + (n<< 1) + (p - '0');
    p=get();
    };
    return n*s;
}
long long power(int a,int b)
{
    long long r=1,x=a;
    if(b<=0)
    return 0;
    while(b)
    {
        if(b&1)r=(r*x)%MOD;
        x=(x*x)%MOD;
        b>>=1;
    }
    return r;
}
bool palindrome(LL n)
{
    LL x=n,rev=0,y;
    while(n)
    {
        y=n%10;
        rev=rev*10+y;
        n/=10;
    }
    if(x==rev)
    return true;
    return false;
}
int main()
{
    LL i,j,k,l,t,p,q,r,w,x,y,ans,b,o,c=0;
    long long a[40]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL,-1,-23};
    t=inp();
    for(k=1;k<=t;k++)
    {
        c=0;
        p=inp();
        q=inp();
        for(i=0;i<40;i++)
        if(a[i]>=p&&a[i]<=q)
        c++;
        printf("Case #%lld: %lld\n",k,c);


    }

return 0;
}
