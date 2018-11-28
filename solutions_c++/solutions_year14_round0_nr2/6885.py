#include<iomanip>
#include<iostream>
using namespace std;
#include<cmath>

int main()
{
int t,u=1;
cin>>t;
while(u<=t)
{
 double c,f,x,y,ans;
ans =0;
 cin>>c>>f>>x;
 y = ceil(((x-c)*f - 2*c)/(c*f));
  if(y<0)
    y = 0;
  for(double i=0;i<y;i++){
   ans = ans + c/(2+i*f);
}
ans = ans + x/(2+y*f);
 cout<<"Case #"<<u<<": "<<setprecision(7)<<fixed<<ans<<endl;  
 u++;
}
}

