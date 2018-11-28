#include<iostream>
#include<cstdlib>
#include<vector>
#include<string>
#include<map>
#include<list>
#include<algorithm>
using namespace std;
#define DEBUG_FLAG 0
#define PRINT(c) (DEBUG_FLAG)?c<<endl:cout<<"";

int main()
{
  int T,A,B,K;
  cin >> T;

  for(int i=0;i<T;i++)
  {
    cin >> A >> B >> K;
    int max=(A>=B ? A : B);
    int min=(A<B ? A : B);
    int flag=0;
    long long result=0;    
    for(int k=min-1;k>=0;--k)
    {
      if(k==min-1)
        flag=1;
      else
        flag=0;
      for(int m=max-1;m>=0;--m)
      {
        if( (k & m) < K)
        {
          PRINT(cout<<"K "<<k<<"M "<<m)
          result++;
        }
      }
    }
             
    cout<<"Case #"<<i+1<<": "<<result<<endl;
  }
}
