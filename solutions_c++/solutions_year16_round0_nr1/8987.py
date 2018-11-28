#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int n;
bool mark[10];

int main()
{
  int t;
  cin>>t;
  for(int q=1;q<=t;q++)
    {
      cin>>n;
      if(n==0)
	{
	  cout<<"Case #"<<q<<": INSOMNIA\n";
	  continue;
	}
      memset(mark,false,sizeof mark);
      int a=0,b=0;
      while(b<10)
	{
	  a+=n;
	  int x=a;
	  while(x>0)
	    {
	      if(!mark[x%10]) b++,mark[x%10]=true;
	      x/=10;
	    }
	}
      cout<<"Case #"<<q<<": "<<a<<endl;
    }
}
