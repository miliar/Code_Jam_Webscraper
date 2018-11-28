#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <math.h>
using namespace std;
double figure(double c,double f,double x)
{
    if(x<=c)
    {
        return x/2;
    }
    int time = ceil((f*(x/c - 1) - 2)/f);
    //cout<<"time:" << time << endl;
    double sum = 0;
    double rate = 2;
    for(int i=0;i<time;i++)
    {
        sum = sum + c/rate;
        rate += f;
    }
   /* for(int i=1;i<=time;i++)
    {
        rate = rate +f;
        sum = sum + c/rate;
    }*/
    sum = sum + x / (rate);
    return sum;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int caseNum;
    double c,f,x;
    int num =1;
    cin>>caseNum;
    while(num<=caseNum)
    {
        cin>>c>>f>>x;
        double outcome = figure(c,f,x);
        cout<<"Case #"<<num<<": ";
        cout<<setiosflags(ios::fixed)<<setiosflags(ios::right)<<setprecision(7);
	    cout<<outcome<<endl;
      //printf("%.7lf", outcome);
     // cout<<endl;
        num++;
    }

    return 0;
}
