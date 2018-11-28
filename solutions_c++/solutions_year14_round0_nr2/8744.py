#include <iostream>
#include<cstdlib>
#include<stdlib.h>
#include<stdio.h>
#include<iomanip>
using namespace std;

int main()
{
    freopen("B-large.in", "r+", stdin);
	freopen("output101.txt", "w+", stdout);

    double c,f,x,s1,s2,sum=0.0,rt=2.0;
    long i,t;
    cin>>t;
    for(i=1;i<=t;i++)
    {
      rt=2.0;
      cin>>c>>f>>x;
      sum=0.0;

      if(x<=c)
      {
        cout <<"Case #"<<i<<": "<< setprecision (7) << fixed <<x/2<<'\n';

      }
      else if((x/2)<=((c/2)+(x/(2+f))))
      {
      cout <<"Case #"<<i<<": "<< setprecision (7) << fixed <<x/2<<'\n';


      }



      else
      {

        while(1)
        {
            s1=(c/rt)+(x/(rt+f));
            s2=(c/rt)+(c/(rt+f))+(x/(rt+f+f));
            if(s1<=s2)
            {
             sum=sum+s1;
             cout <<"Case #"<<i<<": "<< setprecision (7) << fixed <<sum<<'\n';
             //sum=sum+s1;
             sum=0;
             break;
            }
            else
            {
             sum=sum+(c/rt);
             rt=rt+f;
            }

        }



      }






      }










    return 0;
}
// double a=1.123456789;
   // cout<<a;
   // cout << setprecision (7) << fixed << a;

