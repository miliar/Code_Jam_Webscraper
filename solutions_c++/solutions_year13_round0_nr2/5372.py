#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
#include<queue>
#include<set>
using namespace std;
#define PI 2 * acos (0.0)

int Mx[110];
int My[110];
int G[110][110];
int N,M;

bool mower()
{
    int i,j,k;
    for(i=0;i<N;i++)
    {
        for(j=0;j<M;j++)
        {
            if(Mx[i]>G[i][j])
            {
                for(k=0;k<N;k++)
                {
                    if(My[j]>G[k][j])
                        return false;
                }
            }
        }
    }
    return true;
}
void reset()
{
    memset(Mx,0,sizeof(Mx));
    memset(My,0,sizeof(My));
}
int main()
{
    int tc,t=1,i,j;
    freopen("C:\\Users\\talha\\Desktop\\Google_CJ_2013\\B-small-attempt1.in","r",stdin);
    freopen("C:\\Users\\talha\\Desktop\\Google_CJ_2013\\B-small-attempt1.out","w",stdout);
    scanf("%d",&tc);
    while(tc--)
    {
        scanf("%d %d",&N,&M);
        reset();
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                scanf("%d",&G[i][j]);
                Mx[i]=max(Mx[i],G[i][j]);
                My[j]=max(My[j],G[i][j]);
            }
        }
        /*
        for(i=0;i<N;i++)
            cout<<Mx[i]<<" ";
        cout<<endl;
        for(i=0;i<M;i++)
            cout<<My[i]<<" ";
        cout<<endl;
        //*/

        if(mower())
            printf("Case #%d: YES\n",t++);
        else
            printf("Case #%d: NO\n",t++);
    }
    return 0;
}
