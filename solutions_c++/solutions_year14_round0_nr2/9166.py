#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
 double x,c,f,t;
 double total1,total2,time_cookies;
 ifstream fin("B-large.in");
 ofstream fout("output.txt");
 int n;
 fin>>n;
 for(int i=1;i<=n;i++)
 {
  fin>>c;
  fin>>f;
  fin>>x;
   t=2+f;
   time_cookies=c*((double)1/2);
   total1=(x*((double)1/2));
   total2=time_cookies+(x*(1/t));
   while(total2<total1)
   {
    total1=total2;
    time_cookies=time_cookies+(c*(1/t));
    t=t+f;
    total2=time_cookies+(x*(1/t));
   }
   fout<<std::fixed<<setprecision(7)<<"Case #"<<i<<": "<<total1<<endl;
 }

 fin.close();
 fout.close();

return 0;
}
