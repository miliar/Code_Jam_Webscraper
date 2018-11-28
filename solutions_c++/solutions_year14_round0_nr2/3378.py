#include<cstdio>
#include<algorithm>
using namespace std;

double c,f,x;

int main()
{
    int t,n;
    int ca=1;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double s=2;
        double cur=0;
        while(1)
        {
            if(cur+x/s<(cur+c/s+x/(s+f)))
                break;
            else
            {
                cur=cur+c/s;
                s=s+f;
            }
        }
        printf("Case #%d: %.7lf\n",ca++,cur+x/s);
    }
    return 0;
}
