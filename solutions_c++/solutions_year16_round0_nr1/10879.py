#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A.txt","r",stdin);
    freopen("Out.txt","w",stdout);
    int n,a,b,jaw;
    scanf("%d",&n);
    for(int z=1;z<=n;z++)
    {
        bool used[11];
        memset(used,false,sizeof(used));
        scanf("%d",&a);
        for(int i=1;i<=1100;i++)
        {
            bool benar=true;
            b=a*i;
            while(b>0)
            {
                used[b%10]=true;
                b/=10;
            }
            for(int j=0;j<10;j++)if(!used[j])benar=false;
            if(benar){jaw=i;break;}
        }
        if(a==0)printf("Case #%d: INSOMNIA\n",z);
            else printf("Case #%d: %d\n",z,jaw*a);
    }
}
