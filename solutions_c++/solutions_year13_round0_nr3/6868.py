#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
 int res=0,i,j,t,m,n,a[5]={1,4,9,121,484};
 ifstream fi("C-small-attempt1.in");
 ofstream fo("out.txt");
 fi>>t;
 for(j=1;j<=t;j++)
 {
  fi>>n>>m;
  for(i=0;i<5;i++)
  if(a[i]>=n&&a[i]<=m)
  res++;          
  fo<<"Case #"<<j<<": "<<res<<"\n";
  res=0;         
 }   
 return 0;   
}
