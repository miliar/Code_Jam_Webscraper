#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main()
{ int n,i,j,l=1;
  char a[4][4];
  freopen("A-small-attempt0.in","r",stdin);
  cin>>n;
  while(n)
  { for(i=0;i<4;i++)
    { for(j=0;j<4;j++)
      { cin>>a[i][j];
      }
    }  
    getchar();
    int x=0,t=0,o=0,d=0,fl=0;
    if(fl==0)
    for(i=0;i<4;i++)
    { for(j=0;j<4;j++)
      { if(a[i][j]=='X')
        x+=1;
        if(a[i][j]=='O')
        o+=1;
        if(a[i][j]=='T')
        t+=1;
        if(a[i][j]=='.')
        d+=1;
      }
      if(x==4&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }  
      if(o==4&&fl==0)
      { cout<<"Case #"<<l<<": O won\n";
        fl=1;
      }
      if(x==3&&t==1&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }
      if(o==3&&t==1&&fl==0)    
      { cout<<"Case #"<<l<<": Y won\n";
        fl=1; 
      }
      x=0;o=0;t=0;
    }
    
    if(fl==0)  
    for(i=0;i<4;i++)
    { for(j=0;j<4;j++)
      { if(a[j][i]=='X')
        x+=1;
        if(a[j][i]=='O')
        o+=1;
        if(a[j][i]=='T')
        t+=1;
        if(a[j][i]=='.')
        d+=1;
      }
      if(x==4&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }  
      if(o==4&&fl==0)
      { cout<<"Case #"<<l<<": O won\n";
        fl=1;
      }
      if(x==3&&t==1&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }
      if(o==3&&t==1&&fl==0)    
      { cout<<"Case #"<<l<<": Y won\n";
        fl=1; 
      }
      x=0;o=0;t=0;
    }
    if(fl==0)
    { if(a[0][3]=='X')
      x+=1;
      if(a[0][3]=='O')
      o+=1;
      if(a[0][3]=='T')
      t+=1;
      if(a[0][3]=='.')
      d+=1;
      if(a[1][2]=='X')
      x+=1;
      if(a[1][2]=='O')
      o+=1;
      if(a[1][2]=='T')
      t+=1;
      if(a[1][2]=='.')
      d+=1;
      if(a[2][1]=='X')
      x+=1;
      if(a[2][1]=='O')
      o+=1;
      if(a[2][1]=='T')
      t+=1;
      if(a[2][1]=='.')
      d+=1;
      if(a[3][0]=='X')
      x+=1;
      if(a[3][0]=='O')
      o+=1;
      if(a[3][0]=='T')
      t+=1;
      if(a[3][0]=='.')
      d+=1;
      if(x==4&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }  
      if(o==4&&fl==0)
      { cout<<"Case #"<<l<<": O won\n";
        fl=1;
      }
      if(x==3&&t==1&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }
      if(o==3&&t==1&&fl==0)    
      { cout<<"Case #"<<l<<": Y won\n";
        fl=1; 
      }
      x=0;o=0;t=0;
    }
    if(fl==0)
    { if(a[0][0]=='X')
      x+=1;
      if(a[0][0]=='O')
      o+=1;
      if(a[0][0]=='T')
      t+=1;
      if(a[0][0]=='.')
      d+=1;
      if(a[1][1]=='X')
      x+=1;
      if(a[1][1]=='O')
      o+=1;
      if(a[1][1]=='T')
      t+=1;
      if(a[1][1]=='.')
      d+=1;
      if(a[2][2]=='X')
      x+=1;
      if(a[2][2]=='O')
      o+=1;
      if(a[2][2]=='T')
      t+=1;
      if(a[2][2]=='.')
      d+=1;
      if(a[3][3]=='X')
      x+=1;
      if(a[3][3]=='O')
      o+=1;
      if(a[3][3]=='T')
      t+=1;
      if(a[3][3]=='.')
      d+=1;
      if(x==4&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }  
      if(o==4&&fl==0)
      { cout<<"Case #"<<l<<": O won\n";
        fl=1;
      }
      if(x==3&&t==1&&fl==0)
      { cout<<"Case #"<<l<<": X won\n";
        fl=1;
      }
      if(o==3&&t==1&&fl==0)    
      { cout<<"Case #"<<l<<": O won\n";
        fl=1; 
      }
    }
    if(fl==0)
    { if(d!=0)
      cout<<"Case #"<<l<<": Game has not completed\n";
      else
      cout<<"Case #"<<l<<": Draw\n";
    }    
    n--;
    l+=1;
  }
  getch();
  return 0;
}    
