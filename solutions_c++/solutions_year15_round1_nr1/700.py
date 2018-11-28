#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(void)
{
    
  int i,j;
  int num;
  int nTime;
  int nCase=1;
  int ans1;
  int ans2;
  int Mush[1000];
  int interval;
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
    fp1>>Mush[i];
   }
   ans1=0;
   ans2=0;
   interval=0;
   for(i=0;i<num-1;i++)
   {
    if(Mush[i]>Mush[i+1])
    {
     ans1+=(Mush[i]-Mush[i+1]);
    }
   }
   for(i=0;i<num-1;i++)
   {
    interval=interval>(Mush[i]-Mush[i+1])?interval:(Mush[i]-Mush[i+1]);
   }
   for(i=0;i<num-1;i++)
   {
    if(Mush[i]<interval)
    {
     ans2+=Mush[i];
    }
    else
    {
     ans2+=interval;
    }
   }
   
   
   
   fp2<<"Case #"<<nCase<<": "<<ans1<<' '<<ans2<<endl;
   
   nCase++;
   
  }
  
  fp1.close();
  fp2.close();
}
