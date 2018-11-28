#include<iostream>
#include<vector>
#include<fstream>
#include<fstream>
using namespace std;
int main()
{
     ifstream in("A-large.in");
     ofstream out("output.txt");
     int size;
     char nl;
     char arr[4][4];
     bool dot=false,result=false;
     int res[5][2];
     for(int i=0;i<5;i++)
     {
          res[i][0]=0;
          res[i][1]=0;        
     }
     in>>size;
     for(int i=0;i<size;i++)
     {
      for(int count=0;count<5;count++)
     {
          res[count][0]=0;
          res[count][1]=0;        
     }           
          for(int j=0;j<4;j++)
          {
               for(int k=0;k<4;k++)
               {
                    in>>arr[j][k];
                   // cout<<arr[j][k];
                    if(arr[j][k]=='X')
                    {
                         res[j][0]++;
                         res[k][1]++;                  
                    }        
                    else if(arr[j][k]=='O')
                    {
                         res[j][0]--;
                         res[k][1]--;
                    }
                    else if(arr[j][k]=='.')
                    {
                         res[j][0]=res[j][0]+15;
                         res[k][1]=res[k][1]+15;
                         dot=true;
                    }
               }        
               if(arr[j][j]=='X')
               {
                    res[4][0]++;                  
               }
                else if(arr[j][j]=='O')
                {
                         res[4][0]--;
                }
                else if(arr[j][j]=='.')
                {
                     res[4][0]=res[4][0]+15;
                }
                if(arr[j][3-j]=='X')
               {
                    res[4][1]++;                  
               }
                else if(arr[j][3-j]=='O')
                {
                         res[4][1]--;
                }
                else if(arr[j][3-j]=='.')
                {
                     res[4][1]=res[4][1]+15;
                }
          }        
          for(int count=0;count<5;count++)
          {
                if(res[count][0]==3||res[count][1]==3||res[count][0]==4||res[count][1]==4)
                {
                     cout<<"Case #"<<i+1<<": X won";
                     out<<"Case #"<<i+1<<": X won";
                     result=true;
                     
                         cout<<endl;
                         out<<endl;            
                    
                    break;
                }        
                else if(res[count][0]==-3||res[count][1]==-3||res[count][0]==-4||res[count][1]==-4)
                {
                     cout<<"Case #"<<i+1<<": O won";
                     out<<"Case #"<<i+1<<": O won";
                     result=true;
                     
                         cout<<endl;
                         out<<endl;            
                    
                    break;
                }
          }
          if(result==false)
          {
               if(dot==true)                 
               {
                    cout<<"Case #"<<i+1<<": Game has not completed";                              
                    out<<"Case #"<<i+1<<": Game has not completed";
                    
                         cout<<endl;
                         out<<endl;            
                    
               }
               else
               {
                    cout<<"Case #"<<i+1<<": Draw";    
                    out<<"Case #"<<i+1<<": Draw";
                    
                         cout<<endl;
                         out<<endl;            
                        
               }
               
               
          }
          result=false;
          dot=false;
          
     }
     for(int i=0;i<5;i++)
     {
          //cout<<res[i][0]<<"     "<<res[i][1]<<endl;        
     }
}

