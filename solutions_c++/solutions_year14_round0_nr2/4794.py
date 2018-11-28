#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;

double solve(double c,double f,double x,double i,double r); 
int main()
{
    int T;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    double c,f,x;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            cin>>c>>f>>x;
            printf("Case #%d: %.7llf\n",i,solve(c,f,x,0.0,2.0));
    }
    fclose(stdout);
}

double solve(double c,double f,double x,double i,double r)
{
       double t1,t2;
       t1=x/r+i;
       i+=c/r;
       t2=i+x/(r+f);
       if(t1<t2)
         return t1;
       else return solve(c,f,x,i,r+f);
}
