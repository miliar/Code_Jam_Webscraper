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

int main()
{
    LL i,j,k,l,t,p,q,r,w,x,y,ans,b,o;
    char a[6][6];
    t=inp();
    for(k=1;k<=t;k++)
    {
        x=0;o=0;
        bool flag=false;
        for(i=0;i<4;i++){
        scanf("%s",a[i]);}
        //cout<<a[i]<<endl;}
        /*for(i=0;i<4;i++,printf("\n"))
        for(j=0;j<4;j++)
        printf("%c",a[i][j]);*/
        for(i=0;i<4;i++)
        {
            x=0;o=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='X')
                x++;
                else if(a[i][j]=='O')
                o++;
                else if(a[i][j]=='T')
                {x++;o++;}

            }
            if(x==4)
            {
                printf("Case #%d: X won",k);
                goto label;
            }
            else if(o==4)
            {
                printf("Case #%d: O won",k);
                goto label;
            }
        }
        for(j=0;j<4;j++)
        {
            x=0;o=0;
            for(i=0;i<4;i++)
            {
                if(a[i][j]=='X')
                x++;
                else if(a[i][j]=='O')
                o++;
                else if(a[i][j]=='T')
                {x++;o++;}

            }
            if(x==4)
            {
                printf("Case #%d: X won",k);
                flag=true;
                goto label;
            }
            else if(o==4)
            {
                printf("Case #%d: O won",k);
                flag=true;
                goto label;
            }
        }
        x=0;o=0;
        for(i=0;i<4;i++)
        {
               if(a[i][i]=='X')
                x++;
                else if(a[i][i]=='O')
                o++;
                else if(a[i][i]=='T')
                {x++;o++;}
        }
            if(x==4)
            {
                printf("Case #%d: X won",k);
                flag=true;
                goto label;
            }
            else if(o==4)
            {
                printf("Case #%d: O won",k);
                flag=true;
                goto label;
            }
        x=0;o=0;
        for(i=3;i>=0;i--)
        {
               if(a[i][3-i]=='X')
                x++;
                else if(a[i][3-i]=='O')
                o++;
                else if(a[i][3-i]=='T')
                {x++;o++;}
        }
        if(x==4)
            {
                printf("Case #%d: X won",k);
                flag=true;
                goto label;
            }
            else if(o==4)
            {
                printf("Case #%d: O won",k);
                flag=true;
                goto label;
            }
        if(flag==false)
        {
            int c=0;
            for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(a[i][j]=='.')
            c++;
            if(c==0)
            printf("Case #%d: Draw",k);
            else
            printf("Case #%d: Game has not completed",k);
        }
        label:
        printf("\n");

    }

return 0;
}
