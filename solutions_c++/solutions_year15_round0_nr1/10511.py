/**once you accept mediocrity,it suffocates you to life**/
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define s(n) scanf("%d",&n)
#define p(n) printf("%d\n",n)

int b[10],t,n,x,ans,i,smax,l;
char a[10];
int main()
{
    s(t);

    for(l=1;l<=t;l++)
    {
        memset(b,0,sizeof(b));
        memset(a,0,sizeof(a));
        x=0;
        ans=0;
        n=0;
        s(smax);
        scanf("%s",a);

        n=strlen(a);

        for(i=0;i<n;i++)
            b[i]=a[i]-'0';

        int x=0;

        for(i=0;i<n;i++)
        {
            if(b[i]!=0)
            {
                if(x>=i)
                x+=b[i];
            else
                {
                    ans+=(i-x);
                    x+=b[i]+ans;
                }
            }

        }
        printf("Case #%d: %d\n",l,ans);
    }
return 0;
}
