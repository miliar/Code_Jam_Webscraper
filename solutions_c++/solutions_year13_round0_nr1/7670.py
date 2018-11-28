#include<iostream>
using namespace std;

int main()
{
 int test,no=1;
 char a[4][4];
 cin>>test;

 while(test--)
 {
  int x=0,t=0,o=0,dot=0,xwin=0,owin=0;
  for(int i=0;i<4;i++)
   { x=0;o=0;t=0;   
    for(int j=0;j<4;j++)
    {
     cin>>a[i][j];
     //cout<<a[i][j]<<"\n";
     //checking horizontal
     switch(a[i][j])
     {
      case 'X': x++;
           break;
      case 'O': o++;
           break;
      case 'T': t++;
           break;
      case '.': dot++;
           break;           
     }
    }
    if(x==4||(x==3&&a[i][3]=='T')||(x==3&&a[i][0]=='T'))
     xwin=1;
    else if(o==4||(o==3&&a[i][3]=='T')||(o==3&&a[i][0]=='T'))
     owin=1;    
   }
      
    x=0;o=0;t=0;
    //checking vertical
    for(int i=0;i<4;i++)
    {x=0;o=0;t=0;
     for(int j=0;j<4;j++)
     {
      switch(a[j][i])
      {
       case 'X': x++;
           break;
      case 'O': o++;
           break;
      case 'T': t++;
           break;
      case '.': dot++;
           break;
      }
     }
    if(x==4||(x==3&&a[3][i]=='T')||(x==3&&a[0][i]=='T'))
     xwin=1;
    else if(o==4||(o==3&&a[3][i]=='T')||(o==3&&a[0][i]=='T'))
     owin=1;     
    }
    
  //checking left diagonal
  if((a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='O')
      ||(a[0][0]=='T'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='O')
      ||(a[0][0]=='O'&&a[1][1]=='O'&&a[2][2]=='O'&&a[3][3]=='T'))
      owin=1;
      
  else if((a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='X')
      ||(a[0][0]=='T'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='X')
      ||(a[0][0]=='X'&&a[1][1]=='X'&&a[2][2]=='X'&&a[3][3]=='T'))
      xwin=1;
      
  //checking right diagonal
  if((a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='O')
      ||(a[0][3]=='T'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='O')
      ||(a[0][3]=='O'&&a[1][2]=='O'&&a[2][1]=='O'&&a[3][0]=='T'))
      owin=1;
    
  else if((a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='X')
      ||(a[0][3]=='T'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='X')
      ||(a[0][3]=='X'&&a[1][2]=='X'&&a[2][1]=='X'&&a[3][0]=='T'))
      xwin=1;
      
      
  if(xwin==1)
  cout<<"Case #"<<no<<": "<<"X won\n";
  
  else if(owin==1)
  cout<<"Case #"<<no<<": "<<"O won\n";
  
  else if(xwin==0&&owin==0&&dot==0)
  cout<<"Case #"<<no<<": "<<"Draw\n";
  
  else if(xwin==0&&owin==0&&dot!=0)
  cout<<"Case #"<<no<<": "<<"Game has not completed\n";  
  no++;
 }
}
