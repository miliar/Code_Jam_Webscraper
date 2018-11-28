/*Cookie Clicker Alpha*/
#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2_large.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {   double c,f,x;
        cin>>c>>f>>x;
        double time=0,rate=2,a,b;
        while(1)
        {   a=x/rate;
            b=(c/rate)+(x/(rate+f));
            if(a<b)
            {   time+=a;
                break;
            }
            else
            {   time+=(c/rate);
                rate+=f;
            }
        }
        cout<<"Case #"<<cas<<": ";
        printf("%0.7lf\n",time);
        cas++;
    }
    return 0;
}
