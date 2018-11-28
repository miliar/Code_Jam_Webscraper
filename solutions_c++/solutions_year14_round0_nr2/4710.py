#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const double INF = 3000;
const double ESP = 1e-7;
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    int T;
    double C,F,X;
    scanf("%d",&T);
    for(int kase = 1;kase <= T;kase++)
    {
        int N = 3000;
        double t1,t2,t3,tmp = 0,ans = INF,sum = 0,now = 2;
        scanf("%lf%lf%lf",&C,&F,&X);
        while(N--)
        {
             t1 = C/now;     //deng dai shi jian
             t3 = X/now;
             now += F;
             t2 = X/now;    //wang cheng X kuai
             tmp = sum+t3;
             sum += t1;
             ans = min(ans,tmp);
             ans = min(ans,sum+t2);
        }
        printf("Case #%d: %lf\n",kase,ans);
    }
    return 0;


}
