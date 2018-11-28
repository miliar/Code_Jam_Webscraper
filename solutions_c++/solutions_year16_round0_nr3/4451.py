//In the Name of God

#include <bits/stdc++.h>
using namespace std;
typedef long long lol;

lol make(string s,int m)
{
  lol p=1;
  lol ret=0;
  for(int i=0;i<s.length();i++)
    {
      if(s[i]=='1')
	ret+=p;
      p*=m;
    }
  return ret;
}

string bin(int x)
{
  string ret="";
  for(int i=0;i<16;i++)
    if(x&(1<<i))
      ret+='1';
    else
      ret+='0';
  return ret;
}

bool prime(lol x)
{
  if(x<2)
    return true;
  for(lol i=2;i*i<=x;i++)
    if(x%i==0)
      return false;
  return true;
}

lol calc(lol x)
{
  for(int i=2;i*i<=x;i++)
    if(x%i==0)
      return i;
}


int main()
{
  ios::sync_with_stdio(false);
  cout<<"Case #1:"<<endl;
  int tot=0;
  for(int i=0;i<(1<<16);i++)
    {
      vector <lol> ans;
      string s=bin(i);
      if(s[0]!='1' or s[s.length()-1]!='1')
	continue;
      bool can=true;
      for(int j=2;j<=10;j++)
	{
	  lol x=make(s,j);
	  if(prime(x))
	    {
	      can=false;
	      break;
	    }
	  else
	    ans.push_back(calc(x));
	}
      if(can)
	{
	  tot++;
	  reverse(s.begin(),s.end());
	  cout<<s<<" ";
	  for(int j=0;j<ans.size();j++)
	    cout<<ans[j]<<" ";
	  cout<<endl;
	}
      if(tot==50)
	break;
    }
  return 0;
}
