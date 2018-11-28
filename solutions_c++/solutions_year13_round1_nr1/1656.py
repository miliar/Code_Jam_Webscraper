#include <iostream>
#include <vector>
#include <deque>

#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

typedef long long ll;

typedef std::pair<ll,ll> mypair;


int main()
{
  int T;
  
  cin>>T;

  for(int i=0; i<T; ++i)
  {
    
    ll r, t;
    
    cin>>r>>t;
    
    ll y = 0;
    
    ll inner_r = r;
    ll used_paint = 0;
    
    while(true) {
      
      used_paint += 2*inner_r+1;
      
      if(used_paint <= t)
      {
        inner_r += 2;
        ++y;
      }
      else
        break;
      
    }
    
    cout<<"Case #"<<i+1<<": "<<y<<endl;
    
  }
  
	return 0;
}
