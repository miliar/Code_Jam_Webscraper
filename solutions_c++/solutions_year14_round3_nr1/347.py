#include <iostream>
#include <vector>
#include <string>
#include <algorithm>



using namespace std;


long long gcd(long long a,long long b)
{
  if(a<b)
    return gcd(b,a);
  if(b==0)
    return a;
  return gcd(b,a%b);
}


bool m(long long a)
{
  if(a==1)
    return 1;
  if(a%2!=0)
    return 0;/*
  if(a==1)
  return 1;*/
  return m(a/2);
}



int main()
{
  ios::sync_with_stdio(false);
  int T;
  cin>>T;
  for(int i=1;i<=T;i++)
    {
      long long a,b;
      char tmp;
      cin>>a>>tmp>>b;
      //cerr<<"a = "<<a<<" b = "<<b<<endl;
      long long g=gcd(a,b);
      //cerr<<" g = "<<g<<endl;
      a/=g;
      b/=g;
      int j=0;
      if(!m(b))
	{
	  cout<<"Case #"<<i<<": "<<"impossible"<<endl;
	  continue ;
	}
      while(a<b)
	{
	  a*=2;
	  j++;
	}
      cout<<"Case #"<<i<<": "<<j<<endl;
    }
  return 0;
}
