#include<stdio.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<queue>
#include<stdlib.h>

using namespace std;

typedef unsigned long long int LL;

FILE *fin=fopen("in.txt","r");
FILE *fout=fopen("out.txt","w");

int compare(const void *a,const void *b)
{
  return (*(int*)a-*(int*)b);
}

int main()
{
  int T,r,t,count=0,ans=0;
  
  fscanf(fin,"%d",&T);
  
  while(T--)
  {
    fscanf(fin,"%d %d",&r,&t);
    
    count++;
    ans=0;
    
    while(t>0)
    {
      ans++;
      t-=(r+1)*(r+1)-r*r;
      r+=2;
      if(t<0)
	ans--;
    }
    
    fprintf(fout,"Case #%d: %d\n",count,ans);
  }
  
  return 0;
}
 
