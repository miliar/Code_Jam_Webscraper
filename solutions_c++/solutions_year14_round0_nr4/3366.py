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
int solve(vector<double> nami,vector<double> ken)
{
    bool done[nami.size()];
    int n = nami.size();
    for(int i=0;i<n;i++)
    {
      done[i] = false;  
    }
    int count = 0;
    for(int i=0;i<n;i++)
    { bool flag = false;
      for(int j=0;j<n;j++)
      {
        if(!done[j] && ken[j]>nami[i])
        {
          count++;
          done[j] = true;
          flag = true;
          break;
        }
      }
      if(!flag)
      {   
          for(int j=0;j<n;j++)
          {
            if(!done[j]) {
             done[j] = true; break;   
            }
          
          }
      }
    }
      return n-count;
}
int doIt(vector<double> nami,vector<double> ken)
{
  int count = 0;
  int n = nami.size();
  bool done[n];
  for(int i=0;i<nami.size();i++)
  {
    done[i] = false;  
  }
  for(int i=0;i<n;i++)
  {
    bool flag = false;
    for(int j=0;j<n;j++)
    {
        if(!done[j] && nami[j]>ken[i])
        {
          count++;
          done[j] = true;
          flag = true;
          break;
        }
    }
    if(!flag)
    {
      for(int j=0;j<n;j++)
      {
        if(!done[j]) 
        {
          done[j] = true;
          break;
        }
      }
    }
  }
  return count;
}
int main()
{
  int test;
  cin>>test;
  for(int num=1;num<=test;num++)
  {
    int n;
    cin>>n;
    vector<double> a,b;
    double temp;
    for(int i=0;i<n;i++)
    {
        cin>>temp;
        a.push_back(temp);
    }
    for(int i=0;i<n;i++)
    {
        cin>>temp;
        b.push_back(temp);
    }
    sort(a.begin(),a.end());

    // a == naomi ascending order
    sort(b.begin(),b.end());
    int ansB = doIt(a,b);
    // both ascending now
    int ansA = solve(a,b);
    cout<<"Case #"<<num<<": "<<ansB<<" "<<ansA<<endl;
  }
	return 0;	
}
