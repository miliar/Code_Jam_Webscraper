#include<cstdio>
#include<algorithm>
using namespace std;
double x[1000],y[1000];
bool cmp(double a,double b)
{
    return a>b;
}
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int n,T;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%lf",&x[i]);
        for(int i=0;i<n;i++)
            scanf("%lf",&y[i]);
        sort(x,x+n,cmp);
        sort(y,y+n,cmp);
        int c1=0,c2=0;
        for(int i=0;i<n;i++)
            if(x[c1]>y[i])
                c1++;
        for(int i=0;i<n;i++)
            if(y[c2]>x[i])
                c2++;
        printf("case #%d: %d %d\n",I,c1,n-c2);
    }
}
