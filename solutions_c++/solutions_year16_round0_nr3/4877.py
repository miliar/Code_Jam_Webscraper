#include <iostream>
#include <cmath>

using namespace std;

long long prime(long long n)
{
  for (long long i=2;i<=sqrt(n);i++)
    if (n%i==0)
      return i;
  return -1;
}

int main()
{
  cout<<"Case #1:\n";
  int jessica=0;
  for (int i=32769;jessica<50;i+=2)
  {
    int a[16]={0};
    int t=i;
    for (int i=0;i<16;i++)
    {
      a[i]=t%2;
      t/=2;
    }
    /*for (int i=0;i<16;i++)
      cout<<a[i]<<' ';
    cout<<endl;*/
    int b[11]={0};
    bool cony=1;
    for (int j=2;j<=10;j++)
    {
      long long brown=0;
      for (int i=0;i<16;i++)
        brown=brown*j+a[i];
      if (prime(brown)==-1)
      {
        cony=0;
        break;
      }
      b[j]=prime(brown);
     // cout<<brown<<' '<<prime(brown)<<endl;
    }
    if (cony)
    {
      //cout<<jessica;
      for (int i=0;i<16;i++)
        cout<<a[i];
      for (int j=2;j<=10;j++)
        cout<<' '<<b[j];
      cout<<endl;
      jessica++;
      //break;
    }
  }
  return 0;
}
