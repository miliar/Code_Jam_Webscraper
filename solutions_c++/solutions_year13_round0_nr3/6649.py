#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;
long long int a[1001],b[1001],c[1001];
int main()
{
    long long int i,j,x,y,n,t,cnt,k;
     //freopen("C:\\Users\\Defoliate\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\Defoliate\\Desktop\\output.txt","w",stdout);
    k=0;
    j=i-1;
    for(i=1;i*i<1001;i++)
    {
        x=i;
        n=0;
        while(x)
        {
            y=x%10;
            n=n*10 +y;
            x/=10;
        }
        if(n==i) a[k++]=i*i;
       // printf("AK=%lld\n",a[k-1]);
    }
    j=k;
    k=0;
    for(i=0;i<j;i++)
    {
        x=a[i];
        n=0;
        while(x)
        {
            y=x%10;
            n=n*10 +y;
            x/=10;
        }
        if(n==a[i]) c[k++]=a[i];
    }
    //for(i=0;i<k;i++) printf("%lld %lld\n",i,c[i]);
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%d %d",&x,&y);
        cnt=0;
        for(i=0;i<k;i++)
        {
            if(c[i]>=x && c[i]<=y) cnt++;
        }
        printf("Case #%d: %lld\n",cas++,cnt);
    }
    return 0;
}

