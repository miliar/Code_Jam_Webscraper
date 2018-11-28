#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <math.h>
#define MOD 1000000007
#define ll long long
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
using namespace std;
int main()
{
  int t;
  sd(t);
  for(int j=1;j<=t;j++)
  {  
    string s;
    cin>>s;
    int k = 0;
    s = " " + s;
    for (int i = 1 ; i< s.length();i++)
    {
      if(s.at(i)=='-')
      {
        if(s.at(i-1)==' ') k++;
        else if (s.at(i-1)=='+')k+=2;
        else ;
      } 
    }
    cout<<"Case #"<<j<<": "<<k<<endl;
  }
}
  