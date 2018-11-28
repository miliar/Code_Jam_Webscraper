#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

double res[30][30];

double p[20];
int n,k;

void solvetp()
{
    scanf("%d%d",&n,&k);
    for (int i=0; i<n; i++)
        scanf("%lf",&p[i]);
    double ret=0;
    for (int msk=0; msk<1<<n; msk++)
    {
        int pc=0;
        int cp=msk;
        while (cp)
        {
            pc++;
            cp-=cp&-cp;
        }
        if (k!=pc)
            continue;
        //printf("MSK %d\n",msk);
        memset(res,0,sizeof(res));
        res[0][0]=1;
        int cur=0;
        for (int i=0; i<n; i++)
            if (msk&(1<<i))
            {
                //printf("P %d %f\n",i,p[i]);
                for (int j=0; j<=cur; j++)
                {
                    //printf("SPOT %d %d %f\n",j,cur,res[j][cur]);
                    res[j  ][cur+1]+=res[j][cur]*(1-p[i]);
                    res[j+1][cur+1]+=res[j][cur]*p[i];
                    //printf("%f %f\n",res[j][cur+1],res[j+1][cur+1]);
                }
                cur++;
            }
        //printf("RRRRRRRRRRR %f\n",res[k/2][k]);
        if (res[k/2][k]>ret)
            ret=res[k/2][k];
    }
    printf("%.10f\n",ret);
}

int main()
{
    freopen("D:/in.txt","r",stdin);
    freopen("D:/out.txt","w",stdout);
    int tp;
    scanf("%d",&tp);
    for (int itr=1; itr<=tp; itr++)
    {
        printf("Case #%d: ",itr);
        solvetp();
    }

}
