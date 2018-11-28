#include<iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int ca=1;ca<=t;ca++)
    {
      string map[4];
      int dot=0;
      for(int i=0;i<4;i++)
	{
	  cin>>map[i];	  
	}
      int win=-1;
      for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	  {
	    if(map[i][j]=='.')
	      dot++;
	  }
      for(int i=0;i<4;i++)
	{
	  int x=0,o=0,t=0;
	  for(int j=0;j<4;j++)
	    {
	      if(map[i][j]=='X')
		x++;
	      if(map[i][j]=='O')
		o++;
	      if(map[i][j]=='T')
		t++;
	    }
	  if(x+t==4)
	    win=1;
	  else if(o+t==4)
	    win=0;
	  
	  x=0,o=0,t=0;
	  for(int j=0;j<4;j++)
	    {
	      if(map[j][i]=='X')
		x++;
	      if(map[j][i]=='O')
		o++;
	      if(map[j][i]=='T')
		t++;
	    }
	  if(x+t==4)
	    win=1;
	  else if(o+t==4)
	    win=0;
	}
      
      int x=0,o=0,t=0;      
      for(int i=0;i<4;i++)
	{
	  if(map[i][i]=='X')
	    x++;
	  if(map[i][i]=='O')
	    o++;
	  if(map[i][i]=='T')
	    t++;
	}
      if(x+t==4)
	win=1;
      else if(o+t==4)
	win=0;

      x=0,o=0,t=0;      
      for(int i=0;i<4;i++)
	{
	  if(map[3-i][i]=='X')
	    x++;
	  if(map[3-i][i]=='O')
	    o++;
	  if(map[3-i][i]=='T')
	    t++;
	}
      if(x+t==4)
	win=1;
      else if(o+t==4)
	win=0;
      if(win==-1 && dot==0)
	win=2;
      cout<<"Case #"<<ca<<": ";
      if(win==0)
	cout<<"O won"<<endl;
      else if(win==1)
	cout<<"X won"<<endl;
      else if(win==2)
	cout<<"Draw"<<endl;
      else
	cout<<"Game has not completed"<<endl;
    }
}
