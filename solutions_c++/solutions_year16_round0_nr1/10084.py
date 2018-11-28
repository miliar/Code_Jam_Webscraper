#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
  long long int T;
  long long int K;
  cin>>T;
  K=T;
  while(T--)
  {
      long long int n;
      cin>>n;
      if(n==0)
      {
          cout<<"Case #"<<K-T<<": INSOMNIA\n";
          continue;
      }

      long long int counter = 1;
      long long int res;
      int c = 0;
      int array_[10]={0,0,0,0,0,0,0,0,0,0};
      while(c!=10)
      {
          long long int res = n*counter;
          counter++;
          while(res)
          {
              if(array_[res%10] == 0)
              {
                array_[res%10] = 1;
                c++;
              }
              res = res/10;
             // cout<<"s";
          }
          //cout<<"l";
      }
      res = (counter-1)*n;
      cout<<"Case #"<<K-T<<": "<<res<<"\n";


  }
   return 0;
}
