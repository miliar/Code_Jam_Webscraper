#include<iostream>
#include<cstdlib>
#include<vector>
#include<string>
#include<map>
#include<list>
#include<algorithm>
#include<cfloat>
using namespace std;
#define DEBUG_FLAG 0
#define PRINT(c) (DEBUG_FLAG)?c<<endl:cout<<"";

int main()
{
  int T;
  cin >> T;
  long double C,X,F;
  for(int i=0;i<T;i++)
  {
    cin >> C >> F >> X;
    long double last=1.0;
    long double present=0.0;
    long double last_cf;
    int count=0;
    while(1)
    {
      PRINT(cout<<present)
      if(count==0)
      {
        present=X/2.0;
        last=present;
        last_cf=0.0;
        ++count;
        continue;
      }
      last_cf+=(C/(2.0+(count-1)*F));
      present=last_cf+(X/(2.0+count*F));
      
      if(present>last)
      {
        break;
      }
      last=present;
      ++count;
    }
    
    cout.precision(10);
    cout<<"Case #"<<i+1<<": "<<last<<endl;
  }
}
