#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int a[1000009];

int main()
{
    int i,j,k,n,t,cnt,cnta,cntb,ans,tmp,co=1;
    long long m;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %d",&m,&n);
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n);
        cnt=0;
        cnta=cntb=0;
        i=0;
        if(m==1)
            cnt=n;
        else
        {
            while(i<n)
            {
                if(a[i]<m)
                {
                    m=m+a[i++];
                    a[i-1]=cnta;
                    cnta=0;
                }
                else
                {
                    m+=m-1;
                    cnt++;
                    cnta++;
                }
            }
        }
        ans=0;
        //for(i=0;i<n;i++)
            //printf("%d ",a[i]);
        for(i=0;i<n;i++)
        {
            if(!a[i])
                continue;
            //if(a[i]==1 && i==n-1)
                //ans++;
            tmp=0;
            for(j=i+1;j<n;j++)
                tmp+=a[j];
            if(a[i]<=tmp || a[i]<=n-i)
                ans+=a[i];
            else
            {
                ans+=n-i;
                break;
            }
        }
        if(ans<cnt)
        printf("Case #%d: %d\n",co++,ans);
        else
         printf("Case #%d: %d\n",co++,cnt);
    }
    return 0;
}
