#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<utility>

using namespace std;

int main()

{
  int a[4][4],i,j;
  set<int> s;
  int t,c=1;
  cin>>t;
  
  while(c++<=t)
    {
      int m,ans;
      cin>>m;
      s.clear();
      for(i=0;i<4;i++)
	{
	  for(j=0;j<4;j++)
	    {
	      cin>>a[i][j];
	      if(i+1==m)
		{
		  s.insert(a[i][j]);
		}
	    }
	}
      cin>>m;
      int count=0;
      for(i=0;i<4;i++)
	{
	  for(j=0;j<4;j++)
	    {
	      cin>>a[i][j];
	      if(i+1==m)
		{
		  if(s.find(a[i][j])!=s.end())
		    {
		      count++;
		      ans=a[i][j];
		      
		    }
		}
	    }
	}

      if(count==1)
	{
	  cout<<"Case #"<<c-1<<": "<<ans;
	}
      if(count>1)
	{
	  cout<<"Case #"<<c-1<<": Bad magician!";
	}
      if(count==0)
	{
	  cout<<"Case #"<<c-1<<": Volunteer cheated!";
	}
      cout<<endl;
    }
  return 0;
}
	
