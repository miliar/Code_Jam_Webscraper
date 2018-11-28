#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
    int t,i,j,k=1;
    freopen("B-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    double c,f,x,pre,tn;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        pre=2;
        tn=0;
        while(c/pre+x/(pre+f)<x/pre)
        {
            tn+=c/pre;
            pre+=f;
        }
        tn+=x/pre;
        printf("Case #%d: %.7lf\n",k++,tn);
    }
    return 0;
}
