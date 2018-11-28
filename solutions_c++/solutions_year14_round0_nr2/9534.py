#include<iostream>
#include<stdio.h>
using namespace std;
#define INIT 2.0
int main()
{
    int i,j,t,k;
    double c,f,x;
    double time,lasttime;
    cin>>t;

    for (i=1;i<=t;i++)
    {
        cin >> c >> f >> x;
        time = x/(INIT) + 1 ;
        lasttime=time;
        for (j=0;time<=lasttime;j++)
        {
            lasttime=time;
            time = x/(INIT+j*f);
            for(k=0;k<j;k++)
            {
                time += c/(INIT+k*f);
            }
            //cout << time << " " << lasttime << endl;
        }
        printf("Case #%d: %.7lf\n",i,lasttime);
    }


}
