#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
  int i,j;
  int nTime;
  int nCase=1;
  int Smax;
  char chSSpec[1000];
  int SSpec[1000];
  int SumSpec[1000];
  ifstream fp1;
  ofstream fp2;
  fp1.open("input.txt");
  fp2.open("output.txt");
  fp1>>nTime;
  while(nCase<nTime+1)
  {
   fp1>>Smax;
   fp1>>chSSpec;
   for(i=0;i<Smax+1;i++)
   {
    SSpec[i]=chSSpec[i]-'0';
   }
   int k=0;
   for(i=0;i<Smax;i++)
   {
    k+=SSpec[i];
    SumSpec[i]=k;
   }
   int Ans=0;
   for(i=0;i<Smax;i++)
   {
    if(SumSpec[i]<i+1)
    {
     Ans+=(i+1-SumSpec[i]);
     for(j=i+1;j<Smax;j++)
     {
      SumSpec[j]+=(i+1-SumSpec[i]);
     }
    }
   }
   fp2<<"Case #"<<nCase<<": "<<Ans<<endl;
   
   nCase++;
  } 
  fp1.close();
  fp2.close();
    
}
