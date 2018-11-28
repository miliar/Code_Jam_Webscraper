#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

using namespace std;

bool sq(int x)
{
   double a=sqrt(x);     
   int aa=(int)a;
   
   int y=(aa*aa);
   
   if(x==y)
     return true;
     else 
     return false;
     
}


bool pal(int x)
{
 vector <int> v;
 
  while(x!=0)
  {
    v.push_back(x%10);          
    x/=10;           
  }
 
  for(int i=0;i<v.size()/2;++i)
  {
     if(v[i]!=v[v.size()-1-i])
       return false;     
          
  }
       
  return true;   
}


int main()
{
  cout<<"PALINDROME="<<pal(1)<<endl;  
  cout<<"PALINDROME="<<pal(10)<<endl;  
  cout<<"PALINDROME="<<pal(111)<<endl;  
  cout<<"PALINDROME="<<pal(1111)<<endl;  
  cout<<"PALINDROME="<<pal(7)<<endl;  
  cout<<"PALINDROME="<<pal(76)<<endl;  
 
  
  int t;
  ifstream inFile("pc.txt"); 
  string s;
  
  int xwin=0;
  int owin=0;
  int ncom=0;
  
  ofstream myfile;
  myfile.open ("pcout.txt");
  
  if (inFile.is_open())
  {
  
     getline(inFile,s);
     istringstream buffer(s);
     buffer >> t; 
     
     cout<<"Test case="<<t<<endl;
     
     
     for(int it=1;it<=t;++it)
     {
             
         int a,b;    
         getline(inFile,s);
         istringstream buffer(s);
         buffer >>a>>b; 
         
         cout<<"GOT a="<<a<<" B="<<b<<endl;
        
        
       
         int y=0;
           
         for(int i=a;i<=b;++i)
         {
           
           if( pal(i))
           {
              if(sq(i))
              {
                 int tt=(int)sqrt(i);
                 {
                    if(pal(tt))
                    {
                      ++y;
                      cout<<i<<" ";
                    }     
                 }         
                       
              }  
                 
               
           }
                   
                 
         }
         
         cout<<endl;
          
        //END OF ALL CASES.. 
        
        cout<<"Case #"<<it<<": "<<y<<endl;  
        myfile<<"Case #"<<it<<": "<<y<<endl;  
                          
     }
     
     
     
 }
 else
 {
    cout<<"Error reading problem..."<<endl;    
 }
   
   
  inFile.close();  
  myfile.close();   
   


return 1;

}
