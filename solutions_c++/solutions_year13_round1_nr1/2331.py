#include <iostream>
using namespace std;

int main()
{
  int t,i,count;
  long long int j;
  cin>>t;
  long long int r[t],p[t];
  for(i=0;i<t;i++)
    cin>>r[i]>>p[i];
  for(i=0;i<t;i++)
  {
    count=0;
    j=r[i];
    while(p[i]>=(2*j+1))
    {
      p[i]-=(2*j+1);
      count++;
      j+=2;
    }
    cout<<"Case #"<<i+1<<": "<<count<<endl;
  }   
}
   