#include<iostream.h>
#include<conio.h>
#include<fstream.h>
//Input file provided was renamed to a.txt
void main()
{
 int cas,war,dwar,N;
 double n[100],k[100];
 ifstream input;
 ofstream output;
 output.open("output.txt");
 input.open("a.in");
 input>>cas;
 for(int z=0;z<cas;z++)
 {
  war=0;
  dwar=0;
  input>>N;
  for(int i=0;i<N;i++)
   input>>n[i];
  for(i=0;i<N;i++)
   input>>k[i];
  for(i=0;i<N;i++)
  {
   double t1,t2;
   int temp=i;
   int temp1=i;
   for(int j=i;j<N;j++)
   {
    if(n[temp]<n[j])
     temp=j;
     if(k[temp1]<k[j])
     temp1=j;
   }
   t1=n[i];
   n[i]=n[temp];
   n[temp]=t1;
   t2=k[i];
   k[i]=k[temp1];
   k[temp1]=t2;
  }
  int last=N-1;
  int first=0;
  for(i=0;i<N;i++)
  {
    if(n[i]>k[first])
    {
     war++;
     last--;
    }
    else
    {
     first++;
    }
  }
  int last1=N-1;
  for(i=N-1;i>=0;i--)
  {
   if(n[i]>k[last1])
   {
    dwar++;
    last1--;
   }
  }
  output<<"Case #"<<z+1<<": "<<dwar<<" "<<war;
  output<<"\n";
 }
}