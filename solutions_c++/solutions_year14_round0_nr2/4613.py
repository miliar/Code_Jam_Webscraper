#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;
const double eps=1e-8;
int T,n,m;
double c,f,x;
int sign(double x)
{
    if(x<eps&&x>-eps)return 0;
    return x>0?1:-1;
}
int main()
{
//    freopen("ex.in","r",stdin);
//    freopen("ex.out","w",stdout);
    cin>>T;
    int ncase=0;
    while(T--)
    {
        cin>>c>>f>>x;
        double sum=0,cur=2;
        while(1)
        {
            if(sign(c/cur+x/(cur+f)-x/cur)>0)
            {
                sum+=x/cur;break;
            }
            sum+=c/cur;
            cur+=f;
        }
        printf("Case #%d: %.7lf\n",++ncase,sum);
    }
    return 0;
}
