#include<iostream>
#include<fstream>
using namespace std;
int main()
{ifstream in;
ofstream f;
in.open("A-small-attempt7.in");
int n,a;

in>>n;

f.open("file_a.txt");
for(int k=0;k<n;k++)
{
       // cout<<i<<endl;
        a=0;
char arr[4][4];
for(int i=0;i<4;i++)
{
    for(int j=0;j<4;j++)
    {
            in>>arr[i][j];
            
            }    
        }      
     /* for(int i=0;i<4;i++)
{
    for(int j=0;j<4;j++)
    {
            f<<arr[i][j];
            
            }    f<<endl;
        }
        f<<endl;*/
 if((arr[2][2]=='O' || arr[2][2]=='X') && ((arr[0][0]==arr[1][1] && arr[1][1]==arr[2][2] && (arr[3][3]=='T' || arr[3][3]==arr[2][2])) || (arr[2][2]==arr[3][3] && arr[2][2]==arr[1][1] && (arr[0][0]=='T' || arr[0][0]==arr[2][2]))))
 {
                  a=1;      
                  f<<"Case #"<<(k+1)<<": "<<arr[2][2]<<" won\n";   }
if((arr[2][2]=='O' || arr[2][2]=='X') && (a==0) && ((arr[0][3]==arr[1][2] && arr[1][2]==arr[2][1] && (arr[3][0]=='T' || arr[3][0]==arr[1][2])) || (arr[3][0]==arr[2][1] && arr[2][1]==arr[1][2] && (arr[0][3]=='T' || arr[0][3]==arr[1][2]))))
 {
  a=1; 
   f<<"Case #"<<(k+1)<<": "<<arr[2][1]<<" won\n";                        }   
if(a==0)
{
for(int i=0;i<4;i++)
{
 if(((arr[i][0] == arr[i][1] && arr[i][1] == arr[i][2] && (arr[i][3]=='T' || arr[i][3]==arr[i][2]))||(arr[i][1]==arr[i][2] && arr[i][2]==arr[i][3] && (arr[i][0]=='T' || arr[i][0]==arr[i][2]))) && (arr[i][1]=='O' || arr[i][1]=='X'))
             {
                      f<<"Case #"<<(k+1)<<": "<<arr[i][1]<<" won\n";
                      a=1;                             
                           break;                   
                                }      
                   
                   } 
                   }         
   

        

if(a==0)
{
for(int i=0;i<4;i++)
{
 if(((arr[0][i] == arr[1][i] && arr[1][i] == arr[2][i] && (arr[3][i]=='T' || arr[3][i]==arr[1][i]))||(arr[1][i]==arr[2][i] && arr[2][i]==arr[3][i] && (arr[0][i]=='T' || arr[0][i]==arr[2][i]))) && (arr[1][i]=='O' || arr[1][i]=='X'))
             {
                      f<<"Case #"<<(k+1)<<": "<<arr[1][i]<<" won\n";
                      a=1;                             
                           break;                   
                                }      
                   
                   } 
                   }         
   
        if(a==0)
        {
                int l=0;
        for(int i=0;i<4;i++)
{
    for(int j=0;j<4;j++)
    {
            if(arr[i][j]=='.')
            {l=1;
                              f<<"Case #"<<(k+1)<<": "<<"Game has not completed\n";
                              a=1;
                           break;   
                           }
            
            }    cout<<endl;
        if(l==1)
        {break;}
         
        }
        
        }
        if(a==0)
        {
                f<<"Case #"<<(k+1)<<": "<<"Draw\n";
                }
        
 
        }
    
    
    
    
    
   
    return(0);
    }
