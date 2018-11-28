#include<iostream>
using namespace std;
#define inf 99999999
double timex(double f, double c,int x)
{
    double curr_rate=2.0;
    double tot=0.0;
    while(x--)
    {
        tot+= c/curr_rate;
        curr_rate+=f;
    }
    return tot;
}
#include<cstdio>
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("xyzout1.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double min=inf;
        for(int i=0;;i++)
        {
            double temp=timex(f,c,i); //+ x/(2.0 + f*(double)i);
            if(temp>min)break;
            temp=timex(f,c,i) + (x/(2.0 + f*(double)i));
            if(temp<min)min=temp;

        }
        printf("Case #%d %0.7lf\n",test,min);

    }
     fclose(stdin);
    fclose(stdout);
}
