#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
long int bb(long int y)
{
    long int z=0;
    while(y!=0)
     {
       z=(z*10)+y%10;
       y=y/10;     
            }
            return z;
    
    }
int main()
{
  long int count=0,count2=0,x,y; 
  long int r1,r2,m; 
  ifstream in ("raw1.in");

   ofstream out("raw.txt");
   in>>count;
   for(long int i=0;i<count;i++)
   {
        count2=0;
       in>>x>>y;
       for(long int j=x;j<=y;j++)
        {
           m=sqrt(j); 
          if(j==m*m)  
          {
                
            r1=bb(j); 
            r2=bb(m);  
            if(r1==j&&r2==m)
            count2++; 
                
                }
           
          
          
           
            }
            out<<"Case #"<<i+1<<": "<< count2<<endl;
        
        
        
        
        
        }
    
    
    }
