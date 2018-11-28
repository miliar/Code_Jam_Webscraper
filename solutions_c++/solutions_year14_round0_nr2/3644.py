#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream f1;
    ofstream f2;
  f1.open("B.in",ios::in);
  f2.open("PA.in",ios::out);
  f2.precision(7);
  f2.setf(ios::fixed);
  f2.setf(ios::showpoint);
   int t,i1=1,g;
   double c,f,x,t1=0.0,o_r=2.0;
   f1>>t;
   while(i1<=t)
   {    t1=0.0;o_r=2.0;
	   f1>>c>>f>>x;
		while(((c/o_r)+(x/(o_r+f)))<(x/o_r))
         {
	      t1+=((c/o_r));
		  o_r+=f;
         }
		 t1+=(x/o_r);
      f2<<"Case #"<<i1<<": "<<t1<<"\n";
   //printf("%lf\n",t1);
	i1++;
   }
}
