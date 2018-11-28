#include <iostream>
#include <bitset>

using namespace std;
bool digit(long long n, bitset<10> &num)
{
  while(n!=0)
  {
    num[n%10]=false;
    n/=10;
  }
//  cout<<num<<endl;
  return num.any();
}

int main()
{
  long long t,n;
  cin>>t;
  for( int i = 0  ; i < t ; ++i )
  {
    bitset<10> num;
    num.set();
    cin>>n;
    if( n == 0 )
    {
      cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
    }
    else{

    long long c=1,temp=n;
    while( digit(temp,num) )
      temp=n*c++;
    cout<<"Case #"<<i+1<<": "<<n*(c-1)<<endl;
  }
  }
  return 0;
}
