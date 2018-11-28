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
    if((c/r)>=(x/r))
        cout<<"Case #"<<cse<<": "<<fixed<<setprecision(7)<<x/r<<"\n";

    else
        {t_p=(x/r);
        while(1)
            {for(i=0.0;i<i_f;i++)
                    tot+=c/(2+(i*f));
                tot+=x/(2+(i_f*f));
                if(tot<=t_p)
                    {t_p=tot;
                    i_f++;
                    }
                else
                    break;
            tot=0;
            }
        cout<<"Case #"<<cse<<": "<<fixed<<setprecision(7)<<t_p<<"\n";
        }
cse++;i_f=1;r=2.0;tot=0;
}
    return 0;
}