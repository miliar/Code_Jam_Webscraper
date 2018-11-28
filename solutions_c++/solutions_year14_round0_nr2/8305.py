#include<bits/stdc++.h>
using namespace std;

double fun( double c,  double f,  double x, double factor)
{
     double case1=x/f;
     double cost=c/f;
    if((cost + x/(f+factor)) < case1 )
        return (cost +fun(c,f+factor,x,factor));
    else
        return case1;
}

int main()
{
freopen ("input.txt", "r", stdin);
freopen ("output.txt", "w", stdout);
int t,j;
cin>>t;
for(j=1;j<=t;j++)
{
     double c,f,x,ans;
    cin>>c>>f>>x;
    //printf("%0.7f ",c);
    ans=fun(c,2,x,f);
    printf("Case #%d: %.7lf\n",j,ans);
}
}
