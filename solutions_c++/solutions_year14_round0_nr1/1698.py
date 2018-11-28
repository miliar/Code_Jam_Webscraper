#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
int d1[5][5];
int d2[5][5];
int main()
{
    int nc;
    scanf("%d",&nc);
    for(int ic=1;ic<=nc;ic++)
    {
        int a1,a2;
        scanf("%d",&a1);
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)
            scanf("%d",&d1[i][j]);
        scanf("%d",&a2);
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)
            scanf("%d",&d2[i][j]);
        int ans=0;
        for(int ti=1;ti<=16;ti++)
        {
            bool ck=true;
            for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(d1[i][j]==ti)
            {
                if (a1!=i+1)
                    ck=false;
                //printf("debug1:%d\n",i);
            }
            for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(d2[i][j]==ti)
            {
                if (a2!=i+1)
                    ck=false;
                //printf("debug2:%d\n",i);
            }
            if (ck)
            {
                if(ans==0)
                    ans=ti;
                else if (ans>0)
                    ans=-1;
                //printf("debug:%d\n",ti);
            }
        }
        if(ans==-1)
            printf("Case #%d: Bad magician!\n",ic);
        else if (ans==0)
            printf("Case #%d: Volunteer cheated!\n",ic);
        else
            printf("Case #%d: %d\n",ic,ans);
    }
    return 0;
}
