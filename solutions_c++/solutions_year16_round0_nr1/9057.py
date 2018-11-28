#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t,j;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        int n,i,temp,x,ctr=0;
        cin>>n;
        int a[10]={};
        for(i=1;i<=100;i++)
        {
            x=n*i;
            temp=x;
            while(temp!=0)
            {
                if(a[temp%10]!=1)
                {
                    a[temp%10]=1;
                    ctr++;
                }
                if(ctr==10)
                {
                    break;
                }
                temp/=10;
            }
            if(ctr==10)
            {
                break;
            }
        }
        if(ctr!=10)
        {
            printf("Case #%d: INSOMNIA\n",j);
        }
        else
        {
            printf("Case #%d: %d\n",j,x);
        }
    }
    return 0;
}
