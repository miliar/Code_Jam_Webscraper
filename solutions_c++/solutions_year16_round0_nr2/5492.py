//In the Name of God

#include <bits/stdc++.h>
using namespace std;
typedef long long lol;

int main()
{
  ios::sync_with_stdio(false);
  int t;
  cin>>t;
  for(int ttt=0;ttt<t;ttt++)
    {
      string s;
      cin>>s;
      int x=(s[0]!='+'),y=(s[0]!='-');
      for(int i=1;i<s.length();i++)
	{
	  int tmpx=x,tmpy=y;
	  if(s[i]=='-')
	    tmpx=min(y+1,x+2);
	  else
	    tmpy=min(x+1,y+2);
	  x=tmpx;y=tmpy;
	}
      cout<<"Case #"<<ttt+1<<": "<<x<<endl;
    }
  return 0;
}
