#include<cstdio>

using namespace std;

int t,n,a[100],solve[100],ct;
bool is[10];

void reset()
{
    ct=10;
    for(int i=0;i<20;i++)
    {
        a[i]=0;
        solve[i]=0;
    }
    for(int i=0;i<10;i++)
    {
        is[i]=0;
    }
}

void add()
{
    for(int i=1;i<=solve[0];i++)
    {
        solve[i]+=a[i];
        solve[i+1]+=solve[i]/10;
        solve[i]%=10;
        if(is[solve[i]]==0)
        {
            ct--;
            is[solve[i]]=1;
        }
    }
    if(solve[solve[0]+1]!=0)
    {
        solve[0]++;
        if(is[solve[solve[0]]]==0)
        {
            ct--;
            is[solve[solve[0]]]=1;
        }
    }
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {
        scanf("%d",&n);
        reset();
        while(n!=0)
        {
            if(is[n%10]==0)
            {
                ct--;
                is[n%10]=1;
            }
            a[0]++;
            a[a[0]]=n%10;
            solve[0]++;
            solve[solve[0]]=a[a[0]];
            n/=10;
        }
        /*for(int k=solve[0];k>0;k--)
            {
                printf("%d",solve[k]);
            }
            printf("\n\n");
            for(int k=0;k<10;k++)
            {
                printf("%d ",is[k]);
            }
            printf("\n\n");*/
        for(int j=1;j<=1000&&ct>0;j++)
        {
            add();
        }
        printf("Case #%d: ",i);
        if(ct==0)
        {
            for(int j=solve[0];j>0;j--)
            {
                printf("%d",solve[j]);
            }
        }
        else
        {
            printf("INSOMNIA");
        }
        printf("\n");
    }
}
