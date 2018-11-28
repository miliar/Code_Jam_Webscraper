#include<iostream>
#include<fstream>
#include <stdio.h>
#include <math.h>
#include<string>
#include<sstream>
using namespace std;
int bal(int n)
{
    int bal1=0;
    int y=n;
    while(y!=0)
    {
       bal1=bal1*10+y%10;
       y=y/10; 
        
        }
        if(bal1==n)
        return 1;
        return 0;
  
    
}

     
    
    

int main()
{
     int count;
     int c;
     int x,y;
         ifstream in("mmn.in");
    ofstream out("raww.txt");
     
     
    // cout<<"enter # of cases :"<<endl;
     in>>c;

     int s;
     int z;
     
     

     
    for(int j=0;j<c;j++)
    {
             in>>x>>y;
             count=0;
             
      
     for(int i=x;i<=y;i++)
     {
             s=sqrt(i);
             if(s*s==i)
             {
                      if(bal(i)==1)
                      if(bal(s)==1)
                      count++;
                      }
                      }
                      out<<"Case #"<<j+1<<": "<<count<<endl;
                      }
                    
     return 0;
     
     }
     
                      
      
      
      
      
      
      
             
             
             
