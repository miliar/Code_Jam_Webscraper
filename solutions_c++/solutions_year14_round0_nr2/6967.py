#include<iostream>
#include<iomanip>

using namespace std;

double test,c,f,x,r,ans,tx,tc,tm;

int main()
{
  cin>>test;
  
  for(int q=1;q<=test;q++)
  {
    cin>>c>>f>>x;
    r=2.0;
    ans = 0;
    
    while(1)
    {
      tc= c/r;
      tx= x/r;
      
      if(c>=x)
      {
	ans = tx;
	break;
      }
      
      tm = c/f;
      
      if( tc + tm >= tx)
      {
	ans += tx;
	break;
      }
      
      ans += tc;
      r+= f;
    }
    
    std::cout << std::fixed;
    cout<< "Case #"<<q<<": "<<std::setprecision(7)<<ans<<"\n";
  }
}
	
      
      
      