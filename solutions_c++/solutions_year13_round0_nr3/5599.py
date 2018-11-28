#include<iostream>
#include<cmath>
#include<sstream>
using namespace std;
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}



int main()
{
  int count[1001]={0,1,1,1,2};
  for(int i=5;i<1001;i++)
    {
      string tmp = toString(i);
      bool chack =true;
      for(int x=0,y=tmp.size()-1;x<=y;x++,y--)
	if(tmp[x]!=tmp[y])
	  {
	    chack=false;
	  }
      int sq=sqrt(i);
      if(sq*sq!=i)
	chack=false;
      if(chack)
	{
	  tmp = toString(sq);
	  for(int x=0,y=tmp.size()-1;x<=y;x++,y--)
	    if(tmp[x]!=tmp[y])
	      {
		chack=false;
	      }
	}
      if(chack)
	{
	  count[i]=count[i-1]+1;
	  //	  cout<<i<<endl;
	}
      else
	count[i]=count[i-1];
    }
  
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      int a,b;
      cin>>a>>b;
      cout<<"Case #"<<i<<": ";
      cout<<count[b]-count[a-1]<<endl;

    }
}
