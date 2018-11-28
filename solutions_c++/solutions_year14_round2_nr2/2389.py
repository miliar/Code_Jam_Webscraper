#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

#include <fstream>
using std::ifstream;
using std::ofstream;

int value;

int main()
{
    ifstream indata;
    ofstream outdata;
    int t;
    indata.open("B-small-attempt0.in");
    outdata.open("B-small-attempt0.txt");
    indata>>t;
    for(int i=1; i<=t; i++)
    {
      int a,b,k,o=0;
      indata>>a>>b>>k;
      for(int i=0; i<a; i++)
      {
       for(int j=0; j<b; j++)
       {
        int c=i&j;
        if(c<k)
         o+=1;
       }
      }
      outdata<<"Case #"<<i<<": "<<o<<"\n"; 
    }
    
    indata.close();
    outdata.close();
    
//    system("PAUSE");
}
