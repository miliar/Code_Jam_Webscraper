#include<stdio.h>
#define ll long long int
int main()
{
    ll t,k,i,s,ans,t1,r;
    char  a[1005];
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    r=1;
    while(t--)
    {

        ans=0;
        scanf("%lld",&k);
        scanf("%s",a);
        s=a[0]-'0';
      //  printf("%lld\n",s);
        for(i=1;i<=k;i++)
        {
            if(i<=s)
            {
                t1=a[i]-'0';
                s=s+t1;
            }
            else
            {
                ans=ans+i-s;
                t1=a[i]-'0';
                s=i+t1;
            }
        }
        printf("Case #%lld: %lld\n",r,ans);
        r++;
    }
    fclose(stdout);
    return 0;
}
