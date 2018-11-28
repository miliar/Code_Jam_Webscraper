#include<iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  
  int solution[t];
  
  for(int k=1;k<=t;k++)
  {
    int omino=0;
    int row=0;
    int column=0;
    int flag=0;
    int grid=0;
    
    cin>>omino>>row>>column;
    
    grid=row*column;
    
    if(omino>2)
    {
      if(grid==3||grid==4||grid==8)
	flag=0;
      
      else
	if(((grid)%omino)==0)
	  flag=1;
    }
    
    else
    {
      if(((grid)%omino)==0)
	flag=1;
    }
    
  solution[k]=flag;
  }
  
  for(int k=1;k<=t;k++)
  {
    cout<<endl<<"Case #"<<k<<": ";
    
    if(solution[k])
      cout<<"GABRIEL";
    else
      cout<<"RICHARD";
  }
  
return 0;
}
    
    