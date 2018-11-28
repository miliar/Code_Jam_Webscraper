#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>

using namespace std;

int main(void)
{
    
  int i,j,k;
  int num; 
  double X[15];
  double Y[15];
  int nTime;
  int nCase=1;
  int yes,no;
  ifstream fp1;
  ofstream fp2;
  fp1.open("input.txt");
  fp2.open("output.txt");
  fp1>>nTime;
  while(nCase<nTime+1)
  {
   fp1>>num;
   for(i=0;i<num;i++)
   {
    fp1>>X[i]>>Y[i];
   }
   fp2<<"Case #"<<nCase<<":"<<endl;
   if(num<4)
   {
    for(i=0;i<num;i++)
    {
     fp2<<"0"<<endl;
    }
    nCase++;
    continue;
   }
   for(i=0;i<num;i++)
   {
    
    int min=15;
    for(j=0;j<num;j++)
    {
     if(i==j)
     {
      continue;
     }
     yes=0;
     no=0;
     for(k=0;k<num;k++)
     {
      if(k==i||k==j)
      {
       continue;
      }
      if(Y[k]-Y[j]-(Y[i]-Y[j])/(X[i]-X[j])*(X[k]-X[j])>0.0)
      {
       yes++;
      }
      if(Y[k]-Y[j]-(Y[i]-Y[j])/(X[i]-X[j])*(X[k]-X[j])<0.0)
      {
       no++;
      }
      
     }
    
      
     min=min<(yes<no?yes:no)?min:(yes<no?yes:no);
      
     
    }
    fp2<<min<<endl;
    
   }
  
   
   
   nCase++;
   
  }
  
  fp1.close();
  fp2.close();
  system("PAUSE");
}
