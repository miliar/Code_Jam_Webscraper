#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<math.h>

using namespace std;

int main()
{
  unsigned long long int t, k, c, s;
  
  cin>>t;
  for(int i=1; i<=t; i++)
    {
      cin>>k;
      cin>>c;
      cin>>s;
      cout<<"Case #"<<i<<": ";

      for(int j=1; j<=s; j++)
	{
	  cout<<j<<" ";
	}
      cout<<endl;
    }
  
  return 0;
}
