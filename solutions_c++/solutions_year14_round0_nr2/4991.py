#include<iostream>
using namespace std;
#include<iomanip>

int main()
{
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        double c,f,x;
        cin>>c>>f>>x;


        double tf=0.0,m=0.0,cps=2.0;


            while(m<x)
            {
               	double t1;
               	t1=tf+x/cps;
            double t2;
            t2=tf+(c/cps)+x/(f+cps);
            if(t1>t2)
            {
                tf=tf+c/cps;
                cps=cps+f;

            }
            else
            {
                tf=tf+x/cps;
                break;
            }
            }


         cout<<"Case #"<<k<<":"<<" "<<fixed<<setprecision (7)<<tf<<"\n";
    }
    return 0;
}
