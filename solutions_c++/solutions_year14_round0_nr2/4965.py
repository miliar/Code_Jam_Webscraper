#include<iostream>
#include<stdio.h>

using namespace std;
int main()
{
    int t;
    cin>>t;
    double c,f,x,time;
    for(int i=0;i<t;i++)
    {
        double r=2;
        time=0;
        cin>>c>>f>>x;
        while(x/r>(c/r+x/(r+f)))
        {
            time+=c/r;
            r+=f;
        }
        time+=x/r;
        printf("Case #%d: %.7f\n",i+1,time);
    }
}