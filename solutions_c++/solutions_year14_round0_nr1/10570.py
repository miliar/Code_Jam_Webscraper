#include <stdio.h>
#include <string.h>
#include<iostream>

using namespace std;

int main()
{
  int n;cin>>n;int p,q,i,j,k;
  int magic1[4][4],magic2[4][4];
  for(i=0;i<n;i++)
  {
      cin>>p;
      for(j=0;j<4;j++)
      {
          for(int k=0;k<4;k++)
          {
              cin>>magic1[j][k];
          }
      }
      cin>>q;
      for(j=0;j<4;j++)
      {
          for(k=0;k<4;k++)
          {
              cin>>magic2[j][k];
          }
      }
      p--;q--;int count=0; int val=0;
      int t1[4]={magic1[p][0],magic1[p][1],magic1[p][2],magic1[p][3]};
      int t2[4]={magic2[q][0],magic2[q][1],magic2[q][2],magic2[q][3]};
      for(k=0;k<4;k++)
      {
          for(j=0;j<4;j++)
          {
              if(t1[k]==t2[j]){val=t1[k];count++;}
          }
      }
      if(count==1)
      { cout<<"Case #"<<i+1<<": "<<val<<endl; }
      if(count==0)
      { cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl; }
      if(count>1)
      { cout<<"Case #"<<i+1<<": Bad cheated!"<<endl; } 
  }
  return 0;
}
