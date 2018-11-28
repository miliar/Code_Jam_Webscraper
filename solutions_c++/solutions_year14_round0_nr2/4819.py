#include<iostream>
#include<fstream>
#include<iomanip>
#include<vector>
#include<cmath>
using namespace std;

int T;vector<double> v1,v2;
long double v1_out(int k)
{
   long double output=0;
  for(int i=0;i<=k;i++)
    output+=v1[i];
  return output;
}

int main()
{
freopen("B-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
cin>>T;
for(int k=0;k<T;k++)
{
  double C,F,X;       
  cin>>C>>F>>X;
  double cps=2;
  v1.push_back(0.000000);
  v2.push_back(X/cps);
  for(int i=1;i<=X;i++)
  {
   v1.push_back(C/cps); 
   cps+=F;    
   v2.push_back(X/cps);
  }

 long double min=v1_out(0)+v2[0];
 for(int i=0;i<=X;i++)
 {
   if(min>(v1_out(i+1)+v2[i+1]))  
     min=v1_out(i+1)+v2[i+1];
 }      
 cout<<"Case #"<<k+1<<": "<<setprecision(10)<<min<<endl;
 v1.clear();v2.clear(); 
}
return 0;
}
