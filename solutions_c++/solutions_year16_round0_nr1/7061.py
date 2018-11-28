/*Author : Md. Al- Amin
           20th batch
           Dept. of CSE, SUST*/
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<map>
#include<set>
#include<queue>
#include<vector>
#define pi (2*acos(0))
#define SF scanf
#define SFd1(a) scanf("%d",&a)
#define SFd2(a,b) scanf("%d%d",&a,&b)
#define SFd3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define PF printf
#define inf 99999999
#define eps 0.00000001
#define ll long long
#define ull long long unsigned
#define int_max 2147483647
#define int_min -2147483648
#define long_max 9223372036854775807
#define long_min -9223372036854775808
#define fr(i,n) for(i=0;i<n;i++)
#define ms(dp,a) memset(dp,a,sizeof(dp))
#define dist(x1,y1,x2,y2) sqrt( ((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)) )
#define PB push_back
#define mem(arr,val) memset(arr,val,sizeof(arr))

using namespace std;
//int rr[]={1,2,-1,-2,1,2,-1,-2};
//int cc[]={2,1,2,1,-2,-1,-2,-1};
//int rr[]={0,0,1,-1};
//int cc[]={-1,1,0,0};
ll t,p,flag[12],i,j,k,n,cnt,res[1000010];
int main()
{
    freopen("A-large00.in","r",stdin);
    freopen("outcountingsheeplarge.txt","w",stdout);

    for(i=1LL; i<=1000005LL; i++)
    {
        memset(flag,0LL,sizeof(flag));
        cnt=0LL;
        for(j=i;; j+=i)
        {
            k=j;
            while(k!=0LL)
            {
                if(flag[k%10LL]==0LL)
                {
                    flag[k%10LL]=1LL;
                    cnt++;
                }
                k/=10LL;
            }
            if(cnt==10LL)
            {
                res[i]=j;
                break;
            }
        }
    }

    scanf(" %lld",&t);

    for(p=1LL; p<=t; p++)
    {
        scanf(" %lld",&n);
        printf("Case #%lld: ",p);
        if(n==0LL)
            printf("INSOMNIA\n");
        else
            printf("%lld\n",res[n]);

    }

    return 0;
}

