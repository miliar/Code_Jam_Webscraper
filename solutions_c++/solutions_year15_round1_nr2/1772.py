#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <stack>
#include <string>
#include <map>
#include <assert.h>


#define abs(x) ((x)>=0?(x):-(x))
#define i64 long long
#define u32 unsigned int
#define u64 unsigned long long
#define clr(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define SZ(x) x.size()
#define PI acos(-1.0)
#define sqr(x) ((x)*(x))
#define MP(x,y) make_pair(x,y)
#define EPS 1e-11



#define pii pair<int,int>
#define FFF freopen("test","r",stdin)
#define all(a) a.begin(),a.end()

using namespace std;


void output(i64 x)
{
    if(x<0) putchar('-'),x=-x;
    if(x==0)
    {
        putchar('0');
        return;
    }
    int a[20],num=0;
    while(x) a[++num]=x%10,x/=10;
    while(num>0) putchar('0'+a[num--]);
}

inline i64 myInt()
{
    char c=getchar();
    while(!isdigit(c)&&c!='-') c=getchar();
    int flag=1;
    if(c=='-') flag=-1,c=getchar();
    i64 x=0;
    while(isdigit(c))
    {
        x=(x*10)+(c-'0');
        c=getchar();
    }
    if(-1==flag) return -x;
    return x;
}


const int N=1005;


int B,n;
int a[N];

int Ans;

i64 ok(i64 t)
{
    i64 sum=0;
    i64 re=0;
    for(int i=1;i<=B;i++)
    {
        sum+=(t-1)/a[i]+1;
        if(t%a[i]==0) re++;
    }

    if(re!=0&&sum<n&&sum+re>=n)
    {
        for(int i=1;i<=n;i++) if(t%a[i]==0)
        {
            sum++;
            if(sum==n)
            {
                Ans=i;
                return 1;
            }
        }
    }

    return sum;
}
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("ans","w",stdout);

    int T=myInt();
    int num=0;
    while(T--)
    {
        B=myInt();
        n=myInt();



        for(int i=1;i<=B;i++) a[i]=myInt();
        if(n<=B)
        {
            printf("Case #%d: %d\n",++num,n);
            continue;
        }
        i64 low=0,high=1e17;
        Ans=-1;

        while(low<=high)
        {
            i64 M=(low+high)>>1;
            if(ok(M)>=n) high=M-1;
            else low=M+1;

            if(Ans!=-1) break;
        }



        printf("Case #%d: %d\n",++num,Ans);



    }
}
/**
3
2 4
10 5
3 12
7 7 7
3 8
4 2 1
*/
