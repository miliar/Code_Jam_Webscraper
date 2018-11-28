#include <iostream>
#include <cstdio>
#include <vector>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("cookie.out","w",stdout);

    int t;
    cin>>t;

    for(int k=1;k<=t;k++)
    {


     long double c,f,x;
     cin>>c>>f>>x;
     long double div=2.0;

     long double xy=x/div,yz=0,xz=0;
     yz=c/div;
     div+=f;
     xz=x/div;
     long double xyz=yz+xz;

     //cout<<xy<<" "<<yz<<" "<<xz<<" "<<xyz<<endl;
     long double time=0,flag=0;
     time+=yz;

     while(xyz<xy)
     {

         xy=x/div;
         yz=c/div;
         time+=yz;
         div+=f;
         xz=x/div;

         xyz=yz+xz;






     }

     time+=xy-yz;


     printf("Case #%d: ",k);
     printf("%.7Lf\n",time);


    }

return 0;
}
