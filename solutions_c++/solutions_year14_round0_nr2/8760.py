#include<iostream>

using namespace std;


int main()
{
  int n;
  long double C,X,F;
  cin>>n;
  for(int k=1;k<n+1;k++)
  {
    cin>>C>>F>>X;
        long double t=0,curr_rate=2;    
    bool in=0;
    while(C/curr_rate + X/(curr_rate + F) < X/curr_rate )
    {
      in=1;
      t += C/curr_rate;
      curr_rate += F;       
    }
    cout.precision(7);
    cout<<"Case #"<<k<<": ";
    if(!in) cout<<fixed<<X/curr_rate<<endl;    
    else cout<<fixed<<t+X/curr_rate<<endl;
  }
  return 0;
}