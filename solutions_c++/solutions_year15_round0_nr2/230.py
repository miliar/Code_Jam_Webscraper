#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
  int i,j;
  int nTime;
  int nCase=1;
  int D;
  int P[1000];
  ifstream fp1;
  ofstream fp2;
  fp1.open("input.txt");
  fp2.open("output.txt");
  fp1>>nTime;
  while(nCase<nTime+1)
  {
   fp1>>D;
   for(i=0;i<D;i++)
   {
    fp1>>P[i];
   }
   int MaxP=0;
   for(i=0;i<D;i++)
   {
    MaxP=MaxP>P[i]?MaxP:P[i];
   }
   int Ans;Ans=MaxP;
   for(i=1;i<MaxP;i++)
   {
    int k=0;
    for(j=0;j<D;j++)
    {
     k+=(P[j]-1)/i;
    }
    k+=i;
    Ans=Ans<k?Ans:k;
   }
   
   fp2<<"Case #"<<nCase<<": "<<Ans<<endl;
   
   nCase++;
  } 
  fp1.close();
  fp2.close();
    
}
