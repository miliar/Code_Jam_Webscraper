#include<iostream>
#include<cmath>
#include<cstdio>

#define eps 1e-9

using namespace std;

double c,f,x;
int k,t;

int dcmp(double x)
{
    if (x<-eps) return -1;else return x>eps;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b_1.out","w",stdout);
    cin>>t;
    for (int cas=1;cas<=t;cas++)
    {
        cin>>c>>f>>x;
        double sum=c/2,ans=x/2;
        for (int k=0;k<=ceil(x)+100;k++)
        {
            if (dcmp(sum+x/(2+(k+1)*f)-ans)<0)
                ans=sum+x/(2+(k+1)*f);
            sum+=c/(2+(k+1)*f);
        }
        printf("Case #%d: %.7lf\n",cas,ans);
    }
    return 0;
}
