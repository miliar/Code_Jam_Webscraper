#include<iostream>
using namespace std;

int main()
{
  int t;
  cin>>t;
  int sol[t];

  for(int j=1;j<=t;j++)
  {
    int m=0;
    int f=0;
    int s=0;
    string in;
    cin>>m;
    cin>>in;
    
    int le[in.size()];
    
    for(int i=0;i<in.size();i++)
      le[i]=(int)in[i]-48;
    
    for(int i=0;i<in.size();i++)
    {
      if(!i)
      {
	if(!le[i])
	{
	  f++;
	  le[i]+=f;
	}
	
	s+=le[i];
      }
      
      else 
      {
	if(le[i])
	{
	  if(i>s)
	  {
	    f+=(i-s);
	    le[i]+=(i-s);
	  }
	    
	s+=le[i];
	}
      }
    }
    
  sol[j]=f;
  }
  for(int j=1;j<=t;j++)
    cout<<endl<<"Case #"<<j<<": "<<sol[j];
  
return 0;
}
    
    