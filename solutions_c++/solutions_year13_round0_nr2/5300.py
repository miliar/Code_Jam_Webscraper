#include<iostream>
#include<map>
#include<climits>
#include<cstdio>
#include<vector>
#include<stack>
#include<queue>
#include<cstring>

using namespace std;

int main()
{

  int t;
  cin>>t;
  for(int tt=0;tt<t;tt++)
    {
      int n,m;
      cin>>n>>m;

      int a[n][m];

      for(int i=0;i<n;i++)
	  for(int j=0;j<m;j++)
	    cin>>a[i][j];

      // find max for rows
      vector<int> rm(n,INT_MIN);
      for(int i=0;i<n;i++)
	  for(int j=0;j<m;j++)
	    rm[i]=max(rm[i],a[i][j]);
	      
      // find max for cols
      vector<int> cm(m,INT_MIN);
      for(int i=0;i<n;i++)
	  for(int j=0;j<m;j++)
	    cm[j]=max(cm[j],a[i][j]);
	    
	
      bool flag=true;
      // now check for all numbers

      for(int i=0;i<n;i++)
	{
	  for(int j=0;j<m;j++)
	    {
	      bool c1=(rm[i]<=a[i][j]);
	      bool c2=(cm[j]<=a[i][j]);
	      if(!(c1||c2))
		{flag=false;break;}
	    }
	  if(!flag)
	    break;
	}

      cout<<"Case #"<<tt+1<<": ";
      if(flag)
	cout<<"YES\n";
      else
	cout<<"NO\n";
    }


  return 0;
}
