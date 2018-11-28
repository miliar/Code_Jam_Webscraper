#include <iostream>
#include<algorithm>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
   ifstream file("input.txt"); 
   int T;
   double c,f,x,t=0,rate=2;
   file>>T;
   for(int i=1;i<=T;i++)
   {
       file>>c;
       file>>f;
       file>>x;
       while((c/rate + x/(rate+f))<(x/rate))
       {
           t+=(c/rate);
           rate+=f;
       }
       t+=(x/rate);
       cout<<"Case #"<<setiosflags(ios::fixed|ios::showpoint)<<setprecision(7)<<i<<": "<<t<<endl;         
       t=0;
       rate=2;
   }
   file.close();
   return 0;
}
