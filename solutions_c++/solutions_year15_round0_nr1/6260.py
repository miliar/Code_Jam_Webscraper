#include<iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  
  int solution[t];

  for(int k=1;k<=t;k++)
  {
    int max=0;
    int pos=0;
    int flag=0;
    int stood=0;
    int friends=0;
    string input;
    
    cin>>max;
    cin>>input;
    
    int level[input.size()];
    
    for(int i=0;i<input.size();i++)
      level[i]=(int)input[i]-48;
    
    for(int i=0;i<input.size();i++)
    {
      if(!i)
      {
	if(!level[i])
	{
	  friends++;
	  level[i]+=friends;
	}
	
	stood+=level[i];
      }
      
      else 
      {
	if(level[i])
	{
	  if(i>stood)
	  {
	    friends+=(i-stood);
	    level[i]+=(i-stood);
	  }
	    
	stood+=level[i];
	}
      }
    }
    
  solution[k]=friends;
  }
  
  for(int k=1;k<=t;k++)
    cout<<endl<<"Case #"<<k<<": "<<solution[k];
  
return 0;
}
    
    