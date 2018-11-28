#include<iostream>
#include<fstream>
using namespace std;
int main()
{
  ifstream fin; fin.open("input");
  ofstream fout;  fout.open("output");
  unsigned long long nt,i; fin>>nt; 
   for(i=0;i<nt;i++)
     {
          unsigned long long r,t,count=0;
          fin>>r>>t;   cout<<r<<" "<<t<<"\n";
         
         while(1)
          {
            if( t>=((r+1)*(r+1)-(r*r)) )
              {
                 t-=((r+1)*(r+1)-(r*r));
                   r+=2; count++;
              }
            else break;
          } 
                fout<<"Case #"<<i+1<<": "<<count<<"\n";
     }   fin.close(); fout.close();
  
}
