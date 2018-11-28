#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include<cmath>
using namespace std;
int data[6][6],map[20];
int main()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,a,b,i,j,tt=1,ans,tmp;
    scanf("%d",&t);
    while(t--)
    {
        memset(map,0,sizeof(map));
        ans=0;
        scanf("%d",&a);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            scanf("%d",&data[i][j]);
            if(i==a){map[data[i][j]]=1;}
        }

        scanf("%d",&b);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            scanf("%d",&data[i][j]);
            if(i==b)
            {
                if(map[data[i][j]]==1)
                {
                    ans++;tmp=data[i][j];
                }
            }
        }
        if(ans==1)
        printf("Case #%d: %d\n",tt++,tmp);
        else if(ans==0)
        printf("Case #%d: Volunteer cheated!\n",tt++);
        else
        printf("Case #%d: Bad magician!\n",tt++);
    }
    return 0;
}
