#include<iostream>
#include<cstdio>
using namespace std;
bool check(int a[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(a[i]!=1)
            return false;
    }
    return true;
}
int main()
{
    unsigned long long int n,ans,temp,mp;
    int t,i;
    scanf("%d",&t);
    i=1;
    while(t--)
    {
        scanf("%llu",&n);
        int a[10]={0};
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",i++,n);
        }
        else
        {
            ans=n;
            mp=n;
            temp=10;
            while(ans>0)
            {
                a[ans%temp]=1;
                ans=ans/temp;
            }
            for(;;)
            {
                if(check(a,10))
                {
                    printf("Case #%d: %llu\n",i++,n);
                    break;
                }
                n=n+mp;
                ans=n;
                while(ans>0)
                {
                    a[ans%temp]=1;
                    ans=ans/temp;
                }

            }
        }
    }
    return 0;
}
