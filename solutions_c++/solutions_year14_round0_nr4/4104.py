#include<iostream>
#include<iomanip>
#include<fstream>
#include<math.h>
using namespace std;

double naomi[2000],ken[2000];
double naomi2[2000],ken2[2000];
int N;
double nn()
{
 double s=1;
 int i,p;
 for(i=0;i<N;i++)
 {
  if(naomi[i]<s)
  {
  s=naomi[i];
  p=i;
  }
 }
 naomi[p]=1;
 return s;
}


double kn(double n)
{
 double s=1;
 int i,p,c=0;
 for(i=0;i<N;i++)
 {
  if((ken[i]<s)&&(ken[i]>n))
  {
   s=ken[i];
   p=i;
   c++;
  }
 }
 if(c==0)
 {
  for(i=0;i<N;i++)
  {
   if(ken[i]<s)
   {
    s=ken[i];
    p=i;
   }
  }
 }
 ken[p]=1;
 return s;
}

double nd()
{

 double ns=1,ks=1,kl=0;
 double t=0.00000001;
 int i,p=0;
 for(i=0;i<N;i++)
 {
  if(naomi2[i]<ns)
  {
   ns=naomi2[i];
   p=i;
  }
 }
 for(i=0;i<N;i++)
 {
  if(ken2[i]<ks)
  {
   ks=ken2[i];
  }
 }
 for(i=0;i<N;i++)
 {
  if((ken2[i]>kl)&&(ken2[i]!=1))
  {
   kl=ken2[i];
  }
 }
 if(ns>ks)
 {
  naomi2[p]=1;
  return kl+t;
 } 
 if(ns<ks)
 {
  naomi2[p]=1;
  return kl-t;
 }
}


double kd(double n)
{
 double s=1;
 int i,p,c=0;
 for(i=0;i<N;i++)
 {
  if((ken2[i]<s)&&(ken2[i]>n))
  {
   s=ken2[i];
   p=i;
   c++;
  }
 }
 if(c==0)
 {
  for(i=0;i<N;i++)
  {
   if(ken2[i]<s)
   {
    s=ken2[i];
    p=i;
   }
  }
 }
 ken2[p]=1;
 return s;
}



int value(double n,double k)
{
 if(n>k)
   return 1;
 else if(n<k)
   return 0;
 else if(n==k)
   return 2;

}

int main()
{
 ifstream fin;
 ofstream fout;
 fin.open("D-large.in");
 fout.open("Output.txt");
 int T;
 int i,j,k;
 int wd,wn;
 double t1,t2,v;
 fin>>T;
 for(i=0;i<T;i++)
 {
  fin>>N;
  for(j=0;j<N;j++)
  {
   fin>>naomi[j];
   naomi2[j]=naomi[j];
  }
  for(j=0;j<N;j++)
  {
   fin>>ken[j];
   ken2[j]=ken[j];
  }
  wd=0;
  wn=0;
  for(j=0;j<N;j++)
  {
   t1=nd();
   t2=kd(t1);
   if(t1>t2)
    v=1;
   else if(t1<t2)
    v=0;
   else if(t1==t2)
    v=2;
   wd+=v;
   t1=nn();
   t2=kn(t1);
   if(t1>t2)
    v=1;
   else if(t1<t2)
    v=0;
   else if(t1==t2)
    v=2;
   wn+=v;
  }
  fout<<"Case #"<<i+1<<": "<<wd<<" "<<wn<<"\n";
 }
}

