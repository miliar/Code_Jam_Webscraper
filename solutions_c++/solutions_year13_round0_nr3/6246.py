#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
using namespace std;
long int reverse(int x)
{
    int z=0;
    while(x!=0)
     {
       z=(z*10)+x%10;
       x=x/10;     
            }
            return z;
    
    }
int main()
{
  long int count=0,cc=0,x,y,z1,z2,m;  
  ifstream in ("C-small-attempt0.in");
   ofstream out("out.txt");
   string f;
   getline(in,f);
   
   count = atoi(f.c_str());
   for(long int i=0;i<count;i++)
   {
        cc=0;
       in>>x>>y;
       for(long int j=x;j<=y;j++)
        {
           m=sqrt(j); 
          if(j==m*m)  
          {
                
            z1=reverse(j); 
            z2=reverse(m);  
            if(z1==j)
            if(z2==m) 
            cc++; 
                
                }
           
          
          
           
            }
            out<<"Case #"<<i+1<<": "<< cc<<endl;
        
        
        
        
        
        }
    
    
    }
