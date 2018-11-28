#include<iostream>
#include<math.h>
#include<iomanip>
#include<cstdio>
using namespace std;
int main()
{
double c,f,x;
double t_p,tot=0,r=2.0,i_f=1.0,i=0.0;
int t,cse=1;
cin>>t;
while(t--)
{
    scanf("%lf%lf%lf",&c,&f,&x);
  	t_p=(x/r);
        while(1)
            {for(;i<i_f;i++)
                    tot+=c/(r+(i*f));
                if(tot+x/(r+(i_f*f))<=t_p)
                    {t_p=tot+x/(r+(i_f*f));
                    i_f++;
                    }
                else
                    break;
            }
        cout<<"Case #"<<cse<<": "<<fixed<<setprecision(7)<<t_p<<"\n";
cse++;i_f=1;tot=0;r=2.0;i=0;
}
    return 0;
}