#include <stdio.h>
#include<iostream>
#include<stdlib.h>
#include<map>
#include<vector>
int mod=1000000007;
using namespace std;
vector<int> count(10);
map<vector<int>,int> track;
int ans(vector<int> count,int u)
{
 
  if(u==1)
	if (count[1]>0)
	return 1;
	else
	return 0;
  int o1=u;
  if(track.find(count)!=track.end())
    return track[count];
  vector<int> key=count;
  int o2=mod;
  if(count[u]>0)
  {
    --count[u];
    for(int i=1;i<u;++i)
    {
      ++count[i];
      ++count[u-i];
      o2=min(o2,1+ans(count,u));
      --count[i];
      --count[u-i];
    }
    ++count[u];
  }
  else
    o2=ans(count,u-1);
 
  return track[key]=min(o1,o2);
}
int main()
{
  int t;
  cin>>t;
  for(int tt=1;tt<=t;++tt)
  {
    int n;
    cin>>n;
    for(int i=0;i<10;i++)
      count[i]=0;
    for(int i=0;i<n;i++)
    {
      int x;
      cin>>x;
      ++count[x];
    }
    cout<<"Case #"<<tt<<": ";
    cout<<ans(count,9)<<endl;
 
  }
  return 0; 
}

