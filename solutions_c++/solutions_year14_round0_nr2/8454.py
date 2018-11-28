#include <iostream>
#include <cstring>
#include <cstdio>
#include <stdio.h>
using namespace std;


int main()
{
     freopen ("asa.in","r",stdin);
     freopen ("bb.out","w",stdout);
    int t;
    cin>>t;int cas=1;
    while(t--){

    double c,f,x;
    cin>>c>>f>>x;
    /* scanf("%d.%d %d.%d %d.%d",&c1,&c2,&f1,&f2,&x1,&x2);
     double c=c1*100000;
     c+=c2;

     double f=f1*100000;
     f+=f2;

     double x=x1*100000;
     x+=x2;

     double timeTotal=0;
     double t1=0;
     double t2=0;
     double  kol=2*100000;
     */
      double timeTotal=0;
     double t1=0;
     double t2=0;
     double kol = 2.0;
     for(int i=0;;i++)
     {
         t1=( x/(kol ) );
         t2=( c/ (kol) )+(x/(kol+f));
         if(t1>= t2)
         {
             timeTotal+= (c/ (kol));
             kol+=f;
         }
         else
         {
             timeTotal+=t1;
             break;
         }
     }
    cout<<"Case #"<<cas<<": ";
    cas++;
    printf("%.7f\n",timeTotal);
    }
    return 0;
}
