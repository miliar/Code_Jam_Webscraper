#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
int main(){
  int t;
  double c,f,x,ans,y,i;
int l=1;
  cin>>t;
  while(l<=t){
  cin>>c>>f>>x;
  ans =0;
  y = ceil(((x-c)*f-2*c)/(c*f));
if(y<0)
  y =0;
  for(float i=0;i<y;i++)
    ans += c/(2+i*f);
  
  ans += x/(2+y*f);
  cout<<setprecision(7)<<fixed;
  cout<<"Case #"<<l<<": "<<ans<<endl;
  l++;
  }
  return 0;
}
