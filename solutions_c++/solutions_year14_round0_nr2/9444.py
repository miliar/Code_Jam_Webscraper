#include<math.h>
#include<stdio.h>
#include<string.h>
#define MAXN 10000
#define INF (0x7fffffff)
using namespace std;
double C,F,X,index1[MAXN+1],index2[MAXN+1];
int main()
{
    int T;
    scanf("%d",&T);
    for(int CounterT=1; CounterT<=T; CounterT++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        printf("Case #%d: ",CounterT);
        index1[0]=0;
        for(int i=1; i<=MAXN; i++)index1[i]=index1[i-1]+C/(2.0+F*double(i-1));
        index2[0]=index1[0]+X/2.0;
        double ans=index2[0];
        for(int i=0; i<=MAXN; i++)
        {
            index2[i]=index1[i]+X/(2.0+F*double(i));
            if(ans>index2[i])
            {
                ans=index2[i];
            }
        }
        printf("%.7lf\n",ans);
    }
    return 0;
}
