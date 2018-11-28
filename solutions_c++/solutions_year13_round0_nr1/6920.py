#include<stdio.h>
#include<iostream>
#include<string.h>
char a[4][4],ch;
int win1;

bool check (int i , int j , char c)
{
     
     if(a[i][j]==c || a[i][j]=='T')
     return 1;
     else
     return 0;
} 
int func()
{
                    //rows
                    
                    if(check(0,0,ch) && check(0,1,ch) && check(0,2,ch) && check(0,3,ch) )
                    win1=1;
                    else if(check(1,0,ch) && check(1,1,ch) && check(1,2,ch) && check(1,3,ch) )
                    win1=1;
                    else if(check(2,0,ch) && check(2,1,ch) && check(2,2,ch) && check(2,3,ch) )
                    win1=1;
                    else if(check(3,0,ch) && check(3,1,ch) && check(3,2,ch) && check(3,3,ch) )
                    win1=1;
                    
                    //cols
                    else if(check(0,0,ch) && check(1,0,ch) && check(2,0,ch) && check(3,0,ch) )
                    win1=1;
                    else if(check(0,1,ch) && check(1,1,ch) && check(2,1,ch) && check(3,1,ch) )
                    win1=1;
                    else if(check(0,2,ch) && check(1,2,ch) && check(2,2,ch) && check(3,2,ch) )
                    win1=1;
                    else if(check(0,3,ch) && check(1,3,ch) && check(2,3,ch) && check(3,3,ch) )
                    win1=1;
                    
                    // diagonals
                    else if(check(0,0,ch) && check(1,1,ch) && check(2,2,ch) && check(3,3,ch) )
                    win1=1;
                    else if(check(0,3,ch) && check(1,2,ch) && check(2,1,ch) && check(3,0,ch) )
                    win1=1;
                    
    
    return 0;
    
}

int main()
{   int t,m,i,j;
    scanf("%d",&t);
  
    for(m=1;m<=t;m++)
    {
                 
                     win1=0;
                     
                     
                     for(i=0;i<4;i++)
                     scanf("%s",a[i]);
                     
                    //checking for win1 X
                    ch='X';
                    func();
                    
                    if(win1==1)
                    {
                       printf("Case #%d: X won\n",m);
                       continue;        
                               
                    }
                    
                    ch='O';
                    func();
                    
                    if(win1==1)
                    {
                      printf("Case #%d: O won\n",m);         
                      continue;         
                    }
                    int flag=0;
                    
                    for(i=0;i<4;i++)
                    {
                                    for(j=0;j<4;j++)
                                    {
                                                    if(a[i][j]=='.')
                                                    {
                                                    flag=1;
                                                    break;
                                                    }
                                                    
                                    }
                                    if(flag==1)
                                    break;
                                    
                                    
                                    
                    }
                    
                    
                    if(flag==1)
                    printf("Case #%d: Game has not completed\n",m);
                    else
                    printf("Case #%d: Draw\n",m);
                 
    }
    
    return 0;
    }
                     
                     
