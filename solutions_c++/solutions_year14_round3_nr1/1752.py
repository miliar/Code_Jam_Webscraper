//In the name of GOd

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

int gcd(int x,int y)
{
  if(y==0)
    return x;
  if(x%y==0)
    return y;
  return gcd(y,x%y);
}

int main()
{
#define cin fin
#define cout fout
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      string s;
      cin>>s;
      int m=0;
      long long p=0,q=0;
      for(int j=0;j<s.length();j++)
	if(s[j]=='/')
	  {
	    m=j;
	    break;
	  }
      long long t10=1;
      for(int j=m-1;j>=0;j--)
	p+=(s[j]-'0')*t10,t10*=10;
      t10=1;
      for(int j=s.length()-1;j>m;j--)
	q+=(s[j]-'0')*t10,t10*=10;
      int gcds=gcd(q,p);
      p/=gcds;
      q/=gcds;
      cout<<"Case #"<<i<<": ";
      if(p==1)
	{
	  int y=0,ans=0;
	  while(q>1)
	    {
	      if(q%2)
		{
		  cout<<"impossible"<<endl;
		  y=1;
		  break;
		}
	      else
		q/=2,ans++;
	    }
	  if(y==0)
	    cout<<ans<<endl;
	}
      else
	{
	  int y=0,o=0,qp=q;
	  while(qp>1)
	    {
	      if(qp%2)
		{
		  y=1;
		  break;
		}
	      else
		qp/=2,o++;
	    }
	  qp=q;
	  if(y)
	    {
	      cout<<"impossible"<<endl;
	      continue;
	    }
	  y=0;
	  for(int j=1;j<=o;j++)
	    {
	      if(p*2<qp)
		qp/=2;
	      else
		{
		  cout<<j<<endl;
		  y=1;
		  break;
		}
	    }
	  if(y==0)
	    cout<<"impossible"<<endl;
	}
    }
  return 0;
}
