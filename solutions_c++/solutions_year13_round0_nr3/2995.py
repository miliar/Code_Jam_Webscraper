#include<stdio.h>
#include<cstring>
#include<iostream>
using namespace std;
#define clr(a) memset(a,'\0',sizeof(a))
#define MAX 50
int dp[10000];

bool palin(char str[40])
{
    int i,n;
    n=strlen(str);
    for(i=0;i<n;i++)
    {
        if(str[i]!=str[n-1-i])
            return false;
    }
    return true;
}

void check()
{
    int count=0,j=0;
    long long i;
    char str[40];
    bool ans;
    for(i=0;i<MAX;i++)
    {
        clr(str);
        sprintf(str,"%lld",i);
        ans=palin(str);
        if(ans)
        {
            clr(str);
            long long x=i*i;
            sprintf(str,"%lld",x);
            //cout<<" "<<str<<endl;
            ans=palin(str);
            if(ans)
            {
                dp[i*i]=1;
                //cout<<++j<<" "<<i<<endl;
            }
            else
                dp[i*i]=0;
        }
        else
        {
            dp[i*i]=0;
        }
    }
}


int main()
{
    int t,a,b,i,ans,x=0;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);

    check();
    /*
    for(i=0;i<1001;i++)
    {
        if(dp[i]==1)
            cout<<i<<endl;
    }
    */
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        scanf("%d %d",&a,&b);
        for(i=a;i<=b;i++)
        {
            if(dp[i]==1)
                ans++;
        }
        printf("Case #%d: %d\n",++x,ans);
    }
}
