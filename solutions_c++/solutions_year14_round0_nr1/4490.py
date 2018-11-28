//GCJ Q A
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <queue>
using namespace std;
int a[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int Case;
    scanf("%d",&Case);
    for(int ca=1;ca<=Case;++ca)
    {
        int r1,r2,N;
        memset(a,0,sizeof(a));
        scanf("%d",&r1);
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                scanf("%d",&N);
                if(i==r1) a[N]++;
            }
        }
        scanf("%d",&r2);
        for(int i=1;i<=4;++i)
        {
            for(int j=1;j<=4;++j)
            {
                scanf("%d",&N);
                if(i==r2) a[N]++;
            }
        }
        int cnt=0,ans=0;
        for(int i=1;i<=16;++i)
        {
            if(a[i]==2) ans=i,cnt++;
        }
        printf("Case #%d: ",ca);
        if(cnt==1) printf("%d\n",ans);
        else if(cnt>1) printf("Bad magician!\n");
        else if(cnt==0) printf("Volunteer cheated!\n");
    }
    return 0;
}
