#include<bits/stdc++.h>
using namespace std;
int buck[15];
int main()
{
    freopen("A large input.in","r",stdin);
    freopen("A large output.out","w",stdout);
    int n,i,j,chk;
    long long x,y,mem;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%lld",&x);
        for(j=0;j<10;j++)
            buck[j]=0;
        for(y=x,chk=0;;y+=x)
        {
            if(chk&&y==x)
            {
                printf("Case #%d: INSOMNIA\n",i+1);
                break;
            }
            for(mem=y;mem>0;buck[mem%10]++,mem/=10);
            for(j=0;j<10;j++)
                if(!buck[j])
                    break;
            if(j==10)
            {
                printf("Case #%d: %lld\n",i+1,y);
                break;
            }
            chk=1;
        }
    }
}
