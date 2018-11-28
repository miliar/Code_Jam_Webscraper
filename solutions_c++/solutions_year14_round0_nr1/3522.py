#include <iostream>
#include <string>
#include <stdio.h>
#include <algorithm> // binsearch,max(a,b),min(a,b)
#include <math.h> 
#include <queue>
#include <vector>
#include <set>
#include <list>
#include <map> 
#include <string.h> // memset
#include <cstdlib> // abs(int),labs(int),llabs(int),min,max
#include <limits.h> // int_max,int_min,long_long_max,long_long_min
using namespace std;
int solve(vector<int> a,vector<int> b)
{
  int count = 0;
  int temp;
  for(int i=0;i<a.size();i++)
    for(int j=0;j<b.size();j++)
    {
     if(a[i]==b[j])
     {
       count++;
       temp = a[i];
     }
    }
  if(count==1) return temp;
  if(count>1) return -1;
  if(count<=0) return -2;
}
int main()
{
  int test;
  cin>>test;
  for(int i=1;i<=test;i++)
  {
    int ans1,ans2;
    int mat1[4][4];
    int mat2[4][4];
    cin>>ans1;
    for(int j=0;j<4;j++)
      for(int k=0;k<4;k++)
        cin>>mat1[j][k];
    cin>>ans2;
    for(int j=0;j<4;j++)
      for(int k=0;k<4;k++)
        cin>>mat2[j][k];
    vector<int> a1,a2;
    for(int j=0;j<4;j++)
    {
      a1.push_back(mat1[ans1-1][j]);  
      a2.push_back(mat2[ans2-1][j]);  
    }
    int number = solve(a1,a2);
    if(number>0) 
      cout<<"Case #"<<i<<": "<<number<<endl;
    else if(number == -1)
      cout<<"Case #"<<i<<": Bad magician!"<<endl;
    else 
      cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
  }
	return 0;	
}
