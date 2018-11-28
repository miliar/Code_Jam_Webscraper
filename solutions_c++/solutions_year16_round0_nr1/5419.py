//In the Name of God

#include <bits/stdc++.h>
using namespace std;
typedef long long lol;
const int MAXN=1e6+10;
stringstream sst;
int ans[MAXN];

int main()
{
  ios::sync_with_stdio(false);
  for(int i=1;i<=1000000;i++)
    {
      int x=0,j;
      for(j=1;(x+1)!=(1<<10);j++)
	{
	  sst<<(j*i)<<endl;
	  string s;
	  sst>>s;
	  for(int k=0;k<s.length();k++)
	    x|=(1<<(s[k]-'0'));
	}
      ans[i]=i*(j-1);
    }
  
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    {
      int x;
      cin>>x;
      cout<<"Case #"<<i+1<<": ";
      if(x==0)
	cout<<"INSOMNIA"<<endl;
      else
	cout<<ans[x]<<endl;
    }
  return 0;
}
