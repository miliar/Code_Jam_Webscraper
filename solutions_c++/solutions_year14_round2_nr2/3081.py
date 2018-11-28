#include<iostream>
#include<fstream>
using namespace std;
 int main()
 {int i,j,a,b,k,p,q,c=0;
  int n;
  ifstream fin("input.txt");
  ofstream fout("output.txt");
  
  fin>>n;
  for(i=0;i<n;i++)
   { c=0;
     fin>>a;
     fin>>b;
     fin>>k;
     for(j=0;j<a;j++)
        { for(p=0;p<b;p++)
            { q=j&p;
              if(q<k)
			  c++;  
		    } 
        }
     fout<<"Case #"<<i+1<<": "<<c<<"\n";   
     
   }
 }
