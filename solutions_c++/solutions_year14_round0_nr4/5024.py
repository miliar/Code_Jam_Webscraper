#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<utility>
#define P 1e-9


using namespace std;

int main()

{
  int t,count=1;
  cin>>t;
  while(count++<=t)
    {
      int n;
      cin>>n;
      vector<double> u(n),v(n);
      int i,j;
      for(i=0;i<n;i++)
	{
	  cin>>u[i];
	}
      for(i=0;i<n;i++)
	{
	  cin>>v[i];
	}
      sort(v.begin(),v.end());
      sort(u.begin(),u.end());
      i=0,j=0;
      int count1=0;
      while(i<n && j<n)
	{
	  if(v[j]-u[i]>P)
	    {
	      i++;
	      j++;
	      count1++;
	    }
	  else
	    {
	      j++;
	    }
	}
      int count2=0;
      i=0;
      j=0;
      while(i<n && j<n)
	{
	  if(u[i]-v[j]>P)
	    {
	      i++;
	      j++;
	      count2++;
	    }
	  else
	    {
	      i++;
	    }
	}
      cout<<"Case #"<<count-1<<": "<<count2<<" "<<n-count1<<endl;
    }
  return 0;
}
