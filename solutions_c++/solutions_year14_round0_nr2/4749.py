#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,mid,low,high;
    double c,f,x,ans,r,tmp;
    int k = 1;
    scanf("%d",&t);
    while(t--)
    {
        double ans = 1000000000;
        scanf("%lf %lf %lf",&c,&f,&x);
        r = 2;
        low = 0;
        high = x/r+1;
        bool check = true;
        int i = 0;
        while(check)
        {
            tmp = 0;
            check = false;
            for(int j=0;j<i;j++)
            {
                tmp += c/r;
                r+=f;
            }
            tmp += x/r;
            //printf("%lf %d\n",tmp,i);
            if( tmp < ans )
            {
                ans = tmp;
                check = true;
            }
            r = 2;
            i++;
        }
        printf("Case #%d: %.7lf\n",k++,ans);
    }
    return 0;
}
