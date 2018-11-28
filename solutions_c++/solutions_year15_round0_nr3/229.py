#include <cstdlib>
#include <iostream>
#include <fstream>

int QPdt(int a, int b)
{
    if(a<0)
    {
           return -QPdt(-a,b);
    }
    if(b<0)
    {
           return -QPdt(a,-b);
    }
    if(a==1)
    {
            return b;
    }
    if(b==1)
    {
            return a;
    }
    if(a==b)
    {
            return -1;
    }
    if(a==2&&b==3)
    {
            return 4;
    }
   if(a==2&&b==4)
    {
            return -3;
    }
    if(a==3&&b==2)
    {
            return -4;
    }
    if(a==3&&b==4)
    {
            return 2;
    }
    if(a==4&&b==2)
    {
            return 3;
    }
    if(a==4&&b==3)
    {
            return -2;
    }
}

using namespace std;

int main(void)
{
  int i,j;
  int nTime;
  int nCase=1;
  int nL;
  int nX;
  char L[10000];
  ifstream fp1;
  ofstream fp2;
  fp1.open("input.txt");
  fp2.open("output.txt");
  fp1>>nTime;
  while(nCase<nTime+1)
  {
   fp1>>nL>>nX;
  
   fp1>>L;
   if(nX%4==0)
   {
    fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
   }
   int *NumL=new int[8*nL];
   int nChecki=1;
   int nCheckj=1;
   for(i=0;i<nL;i++)
   {
    NumL[i]=L[i]-'g';
    for(j=1;j<8;j++)
    {
     NumL[i+j*nL]=NumL[i];
    }
   }
   int PdtL=1;
   for(i=0;i<nL;i++)
   {
    PdtL=QPdt(PdtL,NumL[i]);
   } 
   if(PdtL==1)
   {
    fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
   }
   if(PdtL==-1&&(nX%2==0))
   {
    fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
   }
  
   if(PdtL==-1)
   {
    for(i=0;i<2*nL;i++)
    {
     nChecki=QPdt(nChecki,NumL[i]);
     if(nChecki==2)
     {
      break;
     }
    }
    if(nChecki!=2||i>=nL*nX-1)
    {
     fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
    }
    for(j=i+1;j<=i+2*nL;j++)
    {
     nCheckj=QPdt(nCheckj,NumL[j]);
     if(nCheckj==3)
     {
      break;
     }
    }
    if(nCheckj!=3||j>=nL*nX-1)
    {
     fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
    }
    fp2<<"Case #"<<nCase<<": YES"<<endl;
    nCase++;
    continue;
   }
   if(nX%2==1)
   {
    fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
   }
   
   for(i=0;i<4*nL;i++)
    {
     nChecki=QPdt(nChecki,NumL[i]);
     if(nChecki==2)
     {
      break;
     }
    }
    if(nChecki!=2||i>=nL*nX-1)
    {
     fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
    }
    for(j=i+1;j<=i+4*nL;j++)
    {
     nCheckj=QPdt(nCheckj,NumL[j]);
     if(nCheckj==3)
     {
      break;
     }
    }
    if(nCheckj!=3||j>=nL*nX-1)
    {
     fp2<<"Case #"<<nCase<<": NO"<<endl;
    nCase++;
    continue;
    }
   
   
   
   fp2<<"Case #"<<nCase<<": YES"<<endl;
   delete []NumL;
   nCase++;
  } 
  fp1.close();
  fp2.close();
    
    system("PAUSE");
}
