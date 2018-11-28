#include<cstdio>
#include<cstring>
using namespace std;
#define sz 300
int ans[sz][sz];
int val[sz];
int main()
{
    freopen("C-small-1-attempt1.in","r",stdin);
    freopen("ret","w",stdout);
    memset(ans,0,sizeof(ans));
    for(int i=2;i<=5;i++)
    for(int j=2;j<=5;j++)
    for(int k=2;k<=5;k++)
    {
        int w=i*36+j*6+k;
        //printf("%d ",w);
        ans[i*j*k][w]++;
        ans[i*j][w]++;
        ans[i*k][w]++;
        ans[j*k][w]++;
        ans[i][w]++;
        ans[j][w]++;
        ans[k][w]++;
        ans[1][w]++;
    }
    //while(1);
    puts("Case #1:");
    int tt,R,N,M,K;scanf("%d%d%d%d%d",&tt,&R,&N,&M,&K);
    //printf("%d %d %d %d\n",R,N,M,K);
    for(int w=0;w<R;w++)
    {
        for(int i=0;i<sz;i++)val[i]=0;
        for(int i=0;i<K;i++)
        {
            int tmp;scanf("%d",&tmp);
            //printf("%d ",tmp);
            for(int j=0;j<sz;j++)if(val[j]!=-1)
            {
                if(ans[tmp][j]>0)
                {
                    //printf("%d %d %d\n",tmp,j,ans[tmp][j]);
                    val[j]+=ans[tmp][j];
                }
                else val[j]=-1;
            }
        }//printf("\n");
        int cc=0;
        for(int i=0;i<sz;i++)if(val[i]>val[cc]){cc=i;}
        //printf("%d ",cc);
        if(cc==0)while(1);
        printf("%d%d%d\n",cc/36,cc%36/6,cc%6);
    }
}
