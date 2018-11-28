#include<cstdio>
using namespace std;
int main()
{
    int t;
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    scanf("%d",&t);
    for(int i=1; i<=t; i++)
    {
        int a[1005]={0};
        int n;
        scanf("%d",&n);
        long long int rate=0,s1=0,s2=0;
        scanf("%d",&a[0]);
        for(int j=1; j<n; j++)
        {
            scanf("%d",&a[j]);
            if(a[j-1]>a[j])
            {
                s1=s1+a[j-1]-a[j];
                if((a[j-1]-a[j])>rate)
                    rate=a[j-1]-a[j];
            }

        }
        //  int s1=0,s2=0;
        for(int j=0; j<n-1; j++)
        {
            if(a[j]>=rate)
                s2=s2+rate;
            else
                s2=s2+a[j];
        }

        printf("Case #%d: %lld %lld\n",i,s1,s2);
    }
    return 0;
}
