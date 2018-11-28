#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
  int i,j;
  int nTime;
  int nCase=1;
  int nX;
  int nR;
  int nC;
  ifstream fp1;
  ofstream fp2;
  fp1.open("input.txt");
  fp2.open("output.txt");
  fp1>>nTime;
  while(nCase<nTime+1)
  {
   fp1>>nX>>nR>>nC;
   if((nR*nC)%nX!=0||nX>6)
   {
    fp2<<"Case #"<<nCase<<": RICHARD"<<endl;
    nCase++;
    continue;
   }
   int ntmp;
   if(nR>nC)
   {
    ntmp=nR;
    nR=nC;
    nC=ntmp;
   }
   if(nX==3)
   {
    if(nR==1)
    {
     fp2<<"Case #"<<nCase<<": RICHARD"<<endl;
    nCase++;
    continue;
    }
   }
   if(nX==4)
   {
    if(nR<3)
    {
     fp2<<"Case #"<<nCase<<": RICHARD"<<endl;
    nCase++;
    continue;
    }
   }
   if(nX==5)
   {
    if(nR<3||(nR==3&&(nR*nC)<30))
    {
     fp2<<"Case #"<<nCase<<": RICHARD"<<endl;
    nCase++;
    continue;
    }
   }
   if(nX==6)
   {
    if(nR<4)
    {
     fp2<<"Case #"<<nCase<<": RICHARD"<<endl;
    nCase++;
    continue;
    }
   }
   
   
   fp2<<"Case #"<<nCase<<": GABRIEL"<<endl;
   
   nCase++;
  } 
  fp1.close();
  fp2.close();
    
}
