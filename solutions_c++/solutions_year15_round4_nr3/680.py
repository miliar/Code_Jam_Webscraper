#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
#define MaxN 1100
#define eps 1e-7
using namespace std;

struct node
{
    double x,y;
};
int cmp(double x)
{
   if (fabs(x) <eps) return 0;
   if (x>0) return 1;
   return -1;
}
node a[MaxN];
int n;
double dis;
double D(node A, node B)
{
    return sqrt((A.x-B.x)*(A.x-B.x)+(A.y-B.y)*(A.y-B.y));
}
int main()
{
    freopen("in.txt","r",stdin);
    int  flag=0;
    double now,tmp,d;
    while (~scanf("%d%lf",&n,&dis))
    {
        flag=0;
        for (int i=0;i<=n;i++)
          scanf("%lf%lf",&a[i].x,&a[i].y);
        now=0.0;
        for (int i=0;i<n;i++)
        {
            tmp=dis-now;
            d=D(a[i],a[i+1]);
            now+=d;

            while (cmp(now-dis)>=0)
            {
                //cout<<now<<' '<<dis<<endl;
                printf("%.02f,%.02f\n",a[i].x+(a[i+1].x-a[i].x)*tmp/d+eps, a[i].y+(a[i+1].y-a[i].y)*tmp/d+eps);
                tmp+=dis;
                now-=dis;
                flag=1;

            }

        }
        if (flag==0) printf("No Such Points.\n");
    }
    return 0;
}
