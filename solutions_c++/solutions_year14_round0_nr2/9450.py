#include <bits/stdc++.h>

using namespace std;

double minm(double a,double b)
{
    if(a<=b)
    return a;
    else
    return b;
}
int counting=0;
double ans(double c, double f,double x,double current)
{
    int t=floor(x/c);
    if(counting==t)
    return x/(current+2.000000);
    else
    {
        counting++;
        return minm(x/(current+2.000000),c/(current+2.000000)+ans(c,f,x,current+f));
    }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k;
    double x,c,f;
    int t;
    cin >> t;
    for(i=1;i<=t;i++)
    {
        counting=0;
        cin >> c >> f >> x;
        cout << "Case #" << i << ": ";
        printf("%.7f\n",ans(c,f,x,0.000000));
    }
    return 0;
}
