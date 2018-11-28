#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
  
  int t;
  ifstream inFile("pa.txt"); 
  string s;
    
 
  ofstream myfile;
  myfile.open ("paout.txt");
  
  if (inFile.is_open())
  {
  
  getline(inFile,s);
 // cout<<"Number of test cases="<<s<<endl;
  
  istringstream buffer(s);
  buffer >> t;
  
  cout<<"Test cases="<<t<<endl;
 
 
 
  for(int it=1;it<=t;++it)
  {
    getline(inFile,s);
    
    
    istringstream buffer1(s);
   
     long long r,p;
     buffer1>>r>>p;
     
     cout<<"r="<<r<<" p="<<p<<endl;
     
     
     //code
     
     
     int o=0;
     long long sum=0;
     
     for(;;)
     {
       long long tt=((r+1)*(r+1))-(r*r);     
       
       if((sum+tt)<=p)
       {
       sum+=tt;     
       ++o;      
       } 
       else 
       break;
           
       r+=2;
       
       
            
     }
     
     
     myfile<<"Case #"<<it<<": "<<o<<endl;
     
     cout<<"o="<<o<<endl;
     
     //code ends here...
     
     
     
     
  } 
  
  
  
 }
 else 
  cout<<"ERROR OPENING FILE"<<endl;


inFile.close();
myfile.close();


 
 return 0;
 
 
}
