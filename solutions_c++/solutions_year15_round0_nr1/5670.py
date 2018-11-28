//------------Author: Aashit Singh-----------//

#include "iostream"
#include "cstring"
#include "cstdlib"
#include "cstdio"
#include "cmath"

using namespace std;

int main(int argc, char const *argv[])
{
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int t,b;
  cin>>t;
  for(b=1;b<=t;b++)
  {
    int smax,a,standing,required;
    standing=required=0;
    cin>>smax;
    string s;
    cin>>s;
    //cout<<"\n"<<s;
    if (s[0]=='0')
    {
      required+=1;
      standing+=1;
    }
    else
    {
      standing+=(s[0]-48);
    }
    for(a=1;a<=smax;a++)
    {
      if(standing>=a)
      {
        standing+=(s[a]-48);
        //cout<<" "<<standing;
      }
      else
      {
        required+=(a-standing);
        standing+=(a-standing)+(s[a]-48);
        //cout<<" "<<standing;
      }
    }
    cout<<"Case #"<<b<<": "<<required<<"\n";
  }
  return 0;
}