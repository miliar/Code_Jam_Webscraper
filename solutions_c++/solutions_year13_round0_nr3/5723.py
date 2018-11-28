#include <iostream>
#include<fstream>
using namespace std;

int main(int argc, char *argv[])
{
    int n,num,i,j,ans=0,flag=0,rev=0,r=0;
    int temp=0;
    int reverse=0;
    int l=0,u=0;int x=1;
    
    ifstream infile; ofstream outfile;
    outfile.open("output.txt");
    infile.open("C-small-attempt1.in");
    
   infile>>n;
    
    
  while(x<=n)
   {
           infile>>l;
              infile>>u;  
              
    while(l<=u)
     {     if(l==1)
              ans=ans+1;  
           
               num=l;
               temp=num;
               
               while(temp){
            r= temp%10;
            rev = (rev*10)+r;
             temp =temp/10;
         }
        
       
         if(num==rev)
         {    for(i=1;i<num;i++)
                 {  if(i*i==num)
                    {  
                     temp=i;
               while(temp){
                           
            r=i%10;
            reverse = (reverse*10) +r;
             temp =temp/10;
         }
         
         if(i==reverse)
         ans=ans+1;
         
         }
         }
         }
         rev=0;reverse=0;
         l++;
         }
         
         outfile<<"Case #"<<x<<": "<< ans<<"\n";
       ans=0;
         x++;
         
         
    
                    
                                         
                    
                    }               
                                      
 
 
 infile.close();
 outfile.close();
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
}
