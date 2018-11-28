#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <vector>
#include <stack>
#include <iostream>
#include <string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;
int main ()
{
READ("A-large.in");
WRITE("out.out");
    
int t ; 
cin >> t;
int flagP =0;
char array[4][4];
string temp="";
string temp2="";


int cnt =1;
int flag=0;
while(cnt<=t)
{
        for(int i=0; i<4; i++)
        {      for(int j=0;j<4 ;j++)
                        cin>> array[i][j];
        }

        for(int i=0; i<4; i++)
        {
                
                for(int j=0; j<4;j++)
                {
                    if(array[i][j]=='.')flagP=1;
                     temp+=array[i][j];   
                     temp2+=array[j][i];
                }
                
                if(temp=="XXXT" || temp=="XXTX" || temp=="XTXX" || temp=="TXXX" || temp=="XXXX" || temp2=="XXXT" || temp2=="XXTX" || temp2=="XTXX" || temp2=="TXXX" || temp2=="XXXX" )
                {
                cout<<"Case #" << cnt <<": X won" <<endl;
                flag=1;
         
                break;
                }
                if(temp=="OOOT" || temp=="OOTO" || temp=="OTOO" || temp=="TOOO" || temp=="OOOO" || temp2=="OOOT" || temp2=="OOTO" || temp2=="OTOO" || temp2=="TOOO" || temp2=="OOOO" )
                {
                cout<<"Case #" << cnt <<": O won" <<endl;
                flag=1;
         
                break;
                }
                temp="";
                temp2="";
             
        }
        if(flag==0)
        {
         temp  += array[0][0];
         temp  += array[1][1];  
         temp  += array[2][2];
         temp  += array[3][3];
        
         temp2 +=array[0][3];
         temp2  +=array[1][2];
         temp2 += array[2][1];
         temp2 += array[3][0];
      
         
         if(temp=="XXXT" || temp=="XXTX" || temp=="XTXX" || temp=="TXXX" || temp=="XXXX"  || temp2=="XXXT" || temp2=="XXTX" || temp2=="XTXX" || temp2=="TXXX" || temp2=="XXXX"  )
         {
         cout<<"Case #" << cnt <<": X won" <<endl;
         flag=1;
         }
         if(temp=="OOOT" || temp=="OOTO" || temp=="OTOO" || temp=="TOOO" || temp=="OOOO" || temp2=="OOOT" || temp2=="OOTO" || temp2=="OTOO" || temp2=="TOOO" ||  temp2=="OOOO" )
         {
         cout<<"Case #" << cnt <<": O won" <<endl;
         flag=1;
         }
        }
         if(flag==0 && flagP==1)
          cout<<"Case #" << cnt <<": Game has not completed" <<endl;
         else if (flag==0 && flagP==0)
          cout<<"Case #" << cnt <<": Draw" <<endl;       
         
         cnt++; 
         flag=flagP=0;
         temp = temp2 ="";
               
}


 /*   while(cin >>n >>m)
    {
              r=0;r2=0,i=1;
              while(true)
              {
                         if(m>=i)
                         {
                                 m=m-i;
                                 i++;
                                 
                         }
                         
                         r=m;
                        // cout<<r<<" "<<i<<endl;
                         if(i>n || r<=0 || i>r )
                         {
                           if(r>0 && i>n)
                           i=1;        
                          else if(r<=0 || i>r)
                          {
                           cout<<r<<endl;
                          break;
                          }
                          
                         }
                         
              }
    }
*/
return 0;
}


