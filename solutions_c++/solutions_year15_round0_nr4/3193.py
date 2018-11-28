#include<iostream>
using namespace std;

int main()
{
  int test;
  cin>>test;
  
  int sol[test];
  
  for(int j=1;j<=test;j++)
  {
    int o=0;
    int r=0;
    int c=0;
    int f=0;
    cin>>o;
    cin>>r;
    cin>>c;
    
    if(o>2)
    {
      if(r*c==3||r*c==4||r*c==8)
	f=0;
      
      else
	if(((r*c)%o)==0)
	  f=1;
    }
    
    else
    {
      if(((r*c)%o)==0)
	f=1;
    }
    
    
  
  
    
    
	
  sol[j]=f;
  }
  
  for(int j=1;j<=test;j++)
  {
    cout<<endl<<"Case #"<<j<<": ";
    
    if(sol[j])
      cout<<"GABRIEL";
    else
      cout<<"RICHARD";
  }
  
return 0;
}
    
    