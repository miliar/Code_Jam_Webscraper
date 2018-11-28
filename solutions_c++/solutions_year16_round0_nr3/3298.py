#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
    int t,n,k;
    int s[110];
    int p=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d:\n",p);
        p++;
        ll a[11]={0};
        s[0]=1;s[n-1]=1;
        for(int i=1;i<n-1;i++)
            s[i]=0;
        for(int i=0;i<k;i++)
        {
            for(int j=0;j<n/2;j++)
            {
                if(i&(1<<j))
                {
                    s[n-2-j]=1;
                    s[1+j]=1;
                }
                else
                {
                    s[n-2-j]=0;
                    s[1+j]=0;
                }
            }
            for(int j=0;j<n;j++)
                printf("%d",s[j]);
            for(int j=3;j<12;j++)
                printf(" %d",j);
            printf("\n");
        }
    }
}
