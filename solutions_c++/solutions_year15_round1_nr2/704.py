#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>

using namespace std;

int Max(int B[], int num)
{
    int i;
    int result=B[0];
    for(i=0;i<num;i++)
    {
     result=result>B[i]?result:B[i];
    }
    return result;
}

int main(void)
{
    
  int i,j,k; 
  int N;
  int num;
  int Bnum;
  double Check;
  int nTime;
  int max;
  int interval;
  int B[1000];
  int nCase=1;
  ifstream fp1;
  ofstream fp2;
  fp1.open("input.txt");
  fp2.open("output.txt");
  fp1>>nTime;
  while(nCase<nTime+1)
  {
   fp1>>num>>N;
   for(i=0;i<num;i++)
   {
    fp1>>B[i];
   }
   max=Max(B,num);
   interval=0;
   for(i=0;i<num;i++)
   {
    interval+=max/B[i];
   }
   i=(N-num)/interval;
   
   for(;;i--)
   {
            j=num;
            for(k=0;k<num;k++)
            {
             
             j+=(int)(((double)i*(double)max)/(double)B[k]);
             }
             
            if(j<N)
            {
             break;
            }        
   } 
   Check=(double)i*(double)max;
  
   
    
   for(Check=(double)i*(double)max;Check<=((double)i+1.0)*(double)max;Check++)
   {
    j=num;
  
    for(k=0;k<num;k++)
    {
    j+=(int)(Check/(double)B[k]);
    }
   
    if(j>=N)
    {
     
     Bnum=j-N;
     for(k=num-1;k>=0;k--)
     {
      if(Bnum!=0&&(fmod(Check,(double)B[k]))==0)
      {
       Bnum--;
       continue;
      }
      if(Bnum==0&&(fmod(Check,(double)B[k]))==0)
      {
       fp2<<"Case #"<<nCase<<": "<<k+1<<endl;
       break;
      }
     }
     
     break;
    }
   }
   
   
   nCase++;
   
  }
  
  fp1.close();
  fp2.close();
}
