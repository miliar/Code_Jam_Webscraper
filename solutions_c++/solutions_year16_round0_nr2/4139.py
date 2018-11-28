#include<iostream>
#include<fstream>
using namespace std;
/*int same(string x)
{
     bool  n,p;
     n=true;
     p=true;
       for(int i=0;i<x.size();i++)
            if(x[i]=='+')
             n=false;
             for(int i=0;i<x.size();i++)
            if(x[i]=='-')
             p=false;
       
                
      if(p==true)
      return 0;
      if(n==true)
      return 1; 
            
}*/
int main()
{
    ifstream in("B-large.in");
    ofstream out("output.txt");
    int testcase;
    in>>testcase;
    string y;
       getline(in,y);
      for(int t=0;t<testcase;t++)
      {
                 out<<"Case #"<<(t+1)<<": ";        
              string x;
               
               getline(in,x);
               int len=x.size();
               int count=0;
              
                for(int i=0;i<x.size();i++)
                { 
                        if(i==(len-1) && x[i]=='-')
                        count++;
                        if(i>0 && x[i-1]=='+' && x[i]=='-')
                        count++;
                        if(i>0 && x[i-1]=='-' && x[i]=='+')
                        count++;
                }             
             out<<count<<endl;                           
      }
    
}
