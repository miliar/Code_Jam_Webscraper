#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <list>
#include <vector>
using namespace std;

int main()
{

    int test,total;
    test=1;
    cin>>total;
 char a[5][5];
    while(test<=total)
     {
         for(int i=0;i<4;i++)
         for(int j=0;j<4;j++)
         cin>>a[i][j];  
         
        
     bool win =false;
     
        bool flag=false;
        for(int i=0;i<4;i++)
          {
              
              if(  (a[i][0]=='T'||a[i][0]=='O')  &&  (a[i][1]=='T'||a[i][0]=='O') && (a[i][2]=='T'||a[i][0]=='O') && (a[i][3]=='T'||a[i][0]=='O'))
              
               {
                   cout<<a[i][0]<<i;;
                   flag=true;
                   break;
                   }
               if(  (a[0][i]=='T'||a[i][0]=='O')  &&  (a[1][i]=='T'||a[1][i]=='O') && (a[2][i]=='T'||a[i][0]=='O') && (a[3][i]=='T'||a[3][i]=='O'))
              
               {
                   cout<<a[i][0]<<i;;
                   flag=true;
                   break;
                   }
              
              }

          
          
          char temp;
          if(flag==true)
             { int j=0;
          
                 win=true;
               
                 temp='O';
                 
                 }
                 
  if(win==false)
    {
          flag=false;
          for(int i=0;i<4;i++)
          {
              
               if(  (a[i][0]=='T'||a[i][0]=='X')  &&  (a[i][1]=='T'||a[i][0]=='X') && (a[i][2]=='T'||a[i][0]=='X') && (a[i][3]=='T'||a[i][0]=='X'))
               {
                   flag=true;
                   break;
                   }
              if(  (a[0][i]=='T'||a[i][0]=='X')  &&  (a[1][i]=='T'||a[1][i]=='X') && (a[2][i]=='T'||a[i][0]=='X') && (a[3][i]=='T'||a[3][i]=='X'))
              
               {
                   cout<<a[i][0]<<i;;
                   flag=true;
                   break;
                   }
              
              }

          
          
          char temp;
          if(flag==true)
             { int j=0;
                 win=true;
                 
                 temp='X';
                 
                 }

  }
  
      if(win==false)
      {    
          
           
           if(  (a[0][0]=='T'||a[0][0]=='O')  &&  (a[1][1]=='T'||a[1][1]=='O') && (a[2][2]=='T'||a[2][2]=='O') && (a[3][3]=='T'||a[3][3]=='O'))
               {
                   win=true;
                   temp='O';
                   
                   
                   }
              
              
              
              
      }    
              if(win==false)
              {
               
               if(  (a[0][3]=='T'||a[0][3]=='O')  &&  (a[1][2]=='T'||a[1][2]=='O') && (a[2][1]=='T'||a[2][1]=='O') && (a[3][0]=='T'||a[3][0]=='O'))
               {
                   win=true;
                   temp='O';
                   
                   }
              
              
              }

     if(win==false)
     {    
          


         
              
              
               if(  (a[0][0]=='T'||a[0][0]=='X')  &&  (a[1][1]=='T'||a[1][1]=='X') && (a[2][2]=='T'||a[2][2]=='X') && (a[3][3]=='T'||a[3][3]=='X'))
               {
                   win=true;
                   temp='X';
              
                   }
              
              
        }
        
        if(win==false)
         {
              
           
               if(  (a[0][3]=='T'||a[0][3]=='X')  &&  (a[1][2]=='T'||a[1][2]=='X') && (a[2][1]=='T'||a[2][1]=='X') && (a[3][0]=='T'||a[3][0]=='X'))
               
               {
                   temp='X';
                   flag=true;

                   }
              
              
              }


          
         if(win==true)
         cout<<"Case #"<<test<<": "<<temp<<" won";
         else
           {bool f=false;
               for(int i=0;i<4;i++)
               for(int j=0;j<4;j++)
               if(a[i][j]=='.')
                 {
                     f=true;
                     break;
                     }
               
           if(f==true)
         cout<<"Case #"<<test<<":"": Game has not completed";
         else
         cout<<"Case #"<<test<<":"": Draw";
     }    
     cout<<"\n";
         test++;

            
               
                  
                     
                        
                           
                              
                                 
                                    
                                       
                                          
                                             
     }



    }

