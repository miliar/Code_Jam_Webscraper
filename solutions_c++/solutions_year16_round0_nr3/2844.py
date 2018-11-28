#include<cstdio>
#include<math.h>
#include<stack>
#include<string.h>
#include<vector>
#include<stdlib.h>
using namespace std;

char s[105];
unsigned long long divisor(unsigned long long x)
{
    unsigned long long i;
    if(x%2==0)
    {
        return 2;
    }
    for(i=3;i<=x/1000000;i+=2)
    {
        //printf("%lld\n",x);
        if(x%i==0&&x!=i)
        {
            return i;
        }
    }
    for(i=999999;i>=2;i--)
    {
        //printf("%d\n",i);
        if(x%i==0&&x!=i)
        {
            //printf("c%d",i);
            return x/i;
        }
    }
    return -1;
}

int a[15];
vector<int>v;
main()
{
    freopen("abc.txt","w",stdout);
    int j;
    int i;
    unsigned long long x,y,x2,xb,g;
    int n;
    int k;
    int p=0,h;
    scanf("%d",&i);
    scanf("%d %d",&n,&k);
    x=pow(2,n-1);
    x++;
    printf("Case #1:\n");
    stack<int>stk;
    int stl;
    while(p<k)
    {
        i=0;
        h=0;
        xb=x;
        //printf("%lld\n",x);
        while(x)
        {
            s[i]='0'+x%2;
            x/=2;
            i++;
        }
        stl=n;
        //printf("%s\n",s);
        for(i=2;i<=10;i++)
        {
            //printf("a");
            x2=0;
            g=1;
            for(j=0;j<=stl-1;j++)
            {
                //printf("b");
                if(s[j]=='1')
                {
                    x2+=g;
                }
                g*=i;
            }
            //printf("%llu\n",x2);
            y=divisor(x2);
            if(y!=-1)
            {
                a[i]=y;
                h++;
            }
            else
            {
                break;
            }
        }
        if(h==9)
        {
           p++;
           for(j=n-1;j>=0;j--)
           {
               //printf("c");
               printf("%c",s[j]);
           }
           for(i=2;i<=10;i++)
           {
               //printf("e");
               printf(" %d",a[i]);
           }
           printf("\n");
        }
        x=xb;
        x+=2;
    }
}
