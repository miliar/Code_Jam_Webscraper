#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

double x,f,c;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int tit,tot;
    for(scanf("%d",&tot),tit=1;tit<=tot;tit++)
    {
        cin>>c>>f>>x;
        double t0=x/2,t1=t0+x/(2+f)+(c-x)/2;
        for(int i=2;t1<t0;i++)
        {
            t0=t1;
            t1=t0+x/(2+i*f)+(c-x)/(2+i*f-f);
        }
        printf("Case #%d: %.7f\n",tit,t0);
    }
	return 0;
}
