#include <iostream>
using namespace std;
long long T,N;
int main()
{
  long long t;
  long long x,y;
  int bj=0;
  int i;
  cin>>T;
  for (t=0; t<T; t++)
  {
    cin>>N;
    if (N==0)
      cout<<"Case #"<<t+1<<": INSOMNIA"<<endl;
    else
    {
      bj=0;
      i=1;
      while (bj!=1023)
      {
        x=i*N;
        while(x!=0)
        {
          y=x%10;
          x/=10;
          bj=bj|(1<<y);
        }
        i++;
      }
      cout<<"Case #"<<t+1<<": "<<N*(i-1)<<endl;
    }
  }
  return 0;
}
