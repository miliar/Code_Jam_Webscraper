#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;

int main()
{
unsigned long long tt,t,n,k,d;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
cin>>tt;
int c1=0,c2=0,i,j,magic=0;
map<int,int> map1;
map<int,int> map2;

for(t=1;t<=tt;t++)
{
  c1=0;
  c2=0;
  magic=0;
  cin>>c1;
  for(i=1;i<=4;i++)
  {
    for(j=1;j<=4;j++)
    {
      cin>>n;
      if(i==c1)
        map1[n]=1;
    } 
  }
  cin>>c2;
  for(i=1;i<=4;i++)
  {
    for(j=1;j<=4;j++)
    {
      cin>>n;
      
      if(i==c2)
      {
          if(map1.find(n)!=map1.end()){
               magic=n;
               map1.erase(n);
          }
      }
    } 
  }
  if(map1.size()==4)
  {
    cout<<"Case #"<<t<<": Volunteer cheated!";
  }
  else if(map1.size()==3)
  {
    cout<<"Case #"<<t<<": "<<magic;   
  }
  else if(map1.size()==0)
  {
    cout<<"Case #"<<t<<": Bad magician!";
  }
  else
  {
    cout<<"Case #"<<t<<": Bad magician!";
  }
  if(t<=tt-1)
  {
    cout<<"\n";
  }
  map1.clear(); 
}
return 0;
}
