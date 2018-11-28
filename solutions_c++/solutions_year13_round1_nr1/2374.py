#include <iostream.h>
#include <fstream.h>
#include <string>
using namespace std;
int main()
{
    int aa;    
    ifstream inn("A-small-attempt0.in");
    ofstream out("output.txt");
    int T;
    inn>>T;
    for (int i=1;i<=T;i++)
       {
             int r,t,a,c=0 ;
             inn>>r;
             inn>>t;
           
             while (t>0)
             {a=0;
              a=((r+1)*(r+1))-(r*r);
              t=t-a;
              c++; 
              r+=2;
              if (t<0)
              c--; 
           
             }
       out<<"Case #"<<i<<": "<<c<<endl;
       
       }
    

cin>>aa; 
   
}
