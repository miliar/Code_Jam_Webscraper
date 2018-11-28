#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int n;
  cin>>n;
  int z;
  for (int a=1;a<=n;a++)
  {
    cin>>z;
    cout<<"Case #"<<a<<": ";
    if (z==0)
    {
      cout<<"INSOMNIA\n";
      continue;
    }
    bool gg=0;
    bool u[10]={0};
    long long c=0;
    while (!gg)
    {
      c+=z;
      long long j=c;
      while (j)
      {
        u[j%10]=1;
        j/=10;
      }
      gg=1;
      for (int i=0;i<=9;i++)
        if (u[i]==0)
          gg=0;
    }
    cout<<c<<endl;
  }
  return 0;
}