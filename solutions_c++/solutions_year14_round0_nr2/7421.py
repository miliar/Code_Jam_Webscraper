#include <iostream>
#include<iomanip>
typedef long double dbl;
using namespace std;

double cookie(dbl C,dbl F,dbl X)
{
 dbl t1,t2,r=2.0,a=0.0,p;
 bool y=true;
 while(1)
 {
     t1=C/r;
     t2=X/(r+F);
     if((t1+t2)*r<X)
       {
        r+=F;
        a+=t1;
        p=t2;
       // cout<<p<<endl;
        y= false;
       }
       else if(y==true)
       {
        t2=X/r;
        p=t2;
        break;
       }
      else
       break;
 }
 return (a+p);
}

int main()
{
    int t;
    cin>>t;
    dbl C,F,X;
    for(int i=0;i<t;i++)
    {
      cin>>C>>F>>X;
      dbl d = cookie(C,F,X);
      cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<d<<endl;
    }
}
/*for(int i=0;i<p;i++)
 {
     t=C/(2+i*F);
     f++;
     q=(2+i*F);
     a+=t;
   // cout<<t<<endl;
     cout<<a<<endl;
     t1=X/q;
     cout<<t1<<endl;
    // if(a>t1)
        //break;
 }
if(p<0){q=1;}
t1=X/(q+F);
return (a+t1);
}*/
