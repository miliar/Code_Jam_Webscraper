#include<iostream>
#include <stdio.h>

using namespace std;

double sumper,sumtime;

double c,f,x;
bool solve()
{
    if(x / (sumper + f) + c / sumper < x / sumper)
        return true;
    return false;
}
int main()
{
    int t;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>t;
    int copt=t;
    while(t--)
    {
        sumper=0.0;
        sumtime=0.0;
        cin>>c>>f>>x;
        sumper=2.0;

        while(solve())
        {
            sumtime+=c/sumper;
            sumper+=f;
        }

        sumtime+=x/sumper;

        printf("Case #%d: %.7lf\n",copt-t,sumtime);
    }
    return 0;
}
