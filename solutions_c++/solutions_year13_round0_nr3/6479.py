#include <iostream>
#include <fstream>
#include <iomanip>
#include <locale>
#include <sstream>
#include <string.h>
#include <stdio.h>
#include <math.h>
using namespace std;


bool chk(int n)
{
    
    int temp = n;
    int reverse = 0;
    
    
    while (temp != 0)
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }
   
   if(reverse == n)
   {
              
              double res= sqrt(n); 

   if ((res * res)== n) 
   {
            int t = (int)res;
            int num = t;
            int r = 0;
            
            while (t != 0)
   {
      r = r * 10;
      r = r + t%10;
      t = t/10;
   }
            
         if( r == num)
         return true; 
         
           
   }
            

            
    
   }
   return false;
}

int main()
{
    fstream myfile;
  myfile.open ("C-small-attempt1.in");
  
  ofstream outputFile("output12.txt");
  
  
  string line;
  if (myfile.is_open()) 
  {
                  
                            getline (myfile,line); // get number first
                   
  }
    
    
int loop,p;
int cases = 0;
string a;    
istringstream convert(line);

(convert >> loop) ;
     
for(p=0; p<loop; p++)
{
 getline (myfile,line);
 a = line;
 
 istringstream iss(a);

    do
    {
               int i,j;
               
        string sub;
        iss >> sub;
        {
        istringstream convert(sub);
       (convert >> i) ;
       }
       
        
        iss >> sub;
        {
        istringstream convert(sub);
       (convert >> j) ;
       }
        
        iss >> sub;
        
        
        /*code*/
        
        int x;
    int count = 0;
    
    for(x=i; x<=j; x++)
    {
             if(chk(x))
             {
                       ++count;
             }
                        
    }
    cout<<"Case #"<<++cases<<": "<<count<<endl;
    outputFile <<"Case #"<<cases<<": "<<count<<endl;
        /*end*/
        
        
    } while (iss);
}   
    
    
    
    
    
    
    system("pause");
return 0;    
}
