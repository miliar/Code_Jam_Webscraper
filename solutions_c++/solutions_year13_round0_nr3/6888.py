#include<iostream>
#include<fstream>
#include<math.h>
#include<conio.h>
using namespace std;
int pallin(int m)
{
    int n,k,arr[100],i=0,rev=0;
   n=m;
   while(n!=0)
   {k=n%10;
   arr[i]=k;
   i++;
   n=n/10;
   }
    
   for(int j=0;j<i;j++)
   rev=rev*10+arr[j];
   
   if(rev==m)
   return 1;
   else
   return 0;
}
int checksq(int m)
{ for(int i=1;i<=sqrt(m);i++)
   { if(i*i==m)
    return 1;}
  return 0;
}
int main()
{   ifstream infile("C-small-attempt2.in");
    
    ofstream outfile("outputnew5.txt");
    
    int A,B,T;
    
    
    
    infile>>T;
    
    
    for(int j=1;j<=T;j++)
    {int cnt=0;
            infile>>A;
            infile>>B;
          
            
    for(int i=A;i<=B;i++)
    {
            if(pallin(i))
            {
                         if(checksq(i))
                         {  
                                      if(pallin(int(sqrt(i))))
                                      {
                                      cnt++;
                                      }
                                      
                         } 
                         
            }
                       
                       }     
  
    outfile<<"Case #"<<j<<": ";
    outfile<<cnt;
    outfile<<"\n";
    
}
infile.close();
outfile.close();
   
}
        
                            
