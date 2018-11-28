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

char arr[110],arr2[110];
int i,j,l,cnt,nowpos,t,p,fg;

int main()
{
    freopen("B-large0000.in","r",stdin);
    freopen("outrevengelarge.txt","w",stdout);

    scanf(" %d",&t);

    for(p=1;p<=t;p++)
    {
        scanf(" %s",arr);
        l=strlen(arr);
        nowpos=l-1;
        cnt=0;
        while(nowpos>=0)
        {
            while(nowpos>=0&&arr[nowpos]=='+')
            {
                nowpos--;
            }
            if(nowpos<0)
                break;
            fg=0;
            for(i=0;i<nowpos&&arr[i]=='+';i++)
            {
                arr[i]='-';
                fg=1;
            }
            cnt+=fg;
            for(i=0;i<=nowpos;i++)
            {
                arr2[i]=arr[i];
            }
            for(i=0,j=nowpos;i<=nowpos&&j>=0;i++,j--)
            {
                if(arr2[i]=='-')
                arr[j]='+';
                else
                arr[j]='-';
            }
            cnt++;
        }
        printf("Case #%d: %d\n",p,cnt);
    }

    return 0;
}
