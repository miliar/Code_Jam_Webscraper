#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,l;
    string  str[]={"XXXX","TXXX","XTXX","XXTX","XXXT","OOOO","TOOO","OTOO","OOTO","OOOT"};
    string chk[10];
    cin>>t;
    for(l=1;l<=t;l++)
    {         
              int k=0,i=0,j=0,flag=0,f=0;
              string s[4];
              for(i=0;i<4;i++)
              {
                              cin>>s[i];
                              chk[k++]=s[i];                         
              }
                                             
               for(i=0;i<4;i++)
               {
                      chk[k]="";
                      for(j=0;j<4;j++)
                      {
                         chk[k]+=s[j][i];           
                               
                      }
                      k++;
               }  
              chk[k]="";
              chk[k+1]="";
                        
                for(i=0;i<4;i++)
               {
                      
                      chk[k]+=s[i][i];
                      chk[k+1]+=s[i][3-i];
                      
               } 
               for(k=0;k<10;k++)
                {
                         for(i=0;i<10;i++)
                         {
                                  if(chk[k]==str[i])
                                  {
                                         flag=1; 
                                         break;
                                  }               
                         }   
                         if(flag==1)
                         break;             
                }
                if(flag==0)
                {
                           for(k=0;k<4;k++)
                           {
                                 for(i=0;i<4;i++)
                                 {          
                                   if(chk[k][i]=='.')
                                   {
                                        f=1;
                                        break;
                                   }
                                 }  
                              if(f==1)
                              break;                             
                            }       
                          if(f==0)
                          {           
                          cout<<"Case #"<<l<<": "<<"Draw"<<endl;
                          }
                          else if(f==1)
                          {
                           cout<<"Case #"<<l<<": "<<"Game has not completed"<<endl;    
                          }     
                }
                else if(flag==1)
                {
                     if(str[i][0]=='X' || str[i][0]=='T')
                     {
                                       cout<<"Case #"<<l<<": "<<"X won"<<endl;
                     }
                     else if( str[i][0]=='O' || str[i][0]=='T')
                     {
                          cout<<"Case #"<<l<<": "<<"O won"<<endl;
                     }
                } 
                }              
                                      
                
                               
              getche();
              return 0;
}                                              
                                                                                         
