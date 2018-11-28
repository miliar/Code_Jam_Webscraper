#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
int main()
{
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas)
    {
        printf("Case #%d: ",cas);
        int n;
        scanf("%d",&n);
        int a[17]={0};
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                int x;
                scanf("%d",&x);
                if(i==n)a[x]++;
            }
        }
        scanf("%d",&n);
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                int x;
                scanf("%d",&x);
                if(i==n)a[x]++;
            }
        }
        int ans=-1;
        for(int i=1;i<=16;++i)
        {
            if(a[i]==2){
                if(ans>0){ans=-2;break;}
                ans=i;
            }
        }
        if(ans==-1)printf("Volunteer cheated!\n");
        else if(ans==-2)printf("Bad magician!\n");
        else printf("%d\n",ans);
    }



    return 0;
}
