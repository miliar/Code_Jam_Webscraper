#include <iostream>
#include <cstdio>

using namespace std;

double decidetime(double ,double, double,int);

int main()
{

    int t,l=1;
    cin>>t;
    while(t>0)
    {
        double c,f,x;
        double v,res=0,res1=0;
        int n=0,i=1;
        cin>>c>>f>>x;
        v=x/2;
        while(n==0)
        {
            res=decidetime(c,f,x,i);
            if(v>res)
            {
                v=res;
            }
            else
            {
                n=1;

            }

            i++;
        }
        printf("Case #%d: %f\n",l,v);
        l++;
        t--;
    }
    return 0;
}

double decidetime(double c,double f,double x,int i)
{
    double res=0;
    int m;
    for(m=0;m<i;m++)
    {
        res=res+c/(2+(m*f));
    }
    res=res+x/(2+(m*f));
    return res;
}
