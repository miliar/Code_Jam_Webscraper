#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
 int t;
 double c,f,x,s,xv,prev1,prev2,curr;
 cin>>t;
 for(int n=1;n<=t;n++)
 {
  cin>>c>>f>>x;
  prev1=x/2;
  prev2=(x/(2+f))+(c/2);
  s=c/2;
  if(prev1<=prev2)
  {
   cout<<"Case #"<<n<<": "<<fixed<<setprecision(7)<<prev1<<"\n";
   continue;
  }
  for(int i=3;i>0;i++)
  {
   s=s+(c/(2+(i-2)*f));
   curr=(x/(2+(i-1)*f))+s;
   if(prev2<=curr && prev2<=prev1)
   {
    cout<<"Case #"<<n<<": "<<fixed<<setprecision(7)<<prev2<<"\n";
    break;
   }
   else
   {
    prev1=prev2;
    prev2=curr;
   }
  }
 }
 return 0;
} 
