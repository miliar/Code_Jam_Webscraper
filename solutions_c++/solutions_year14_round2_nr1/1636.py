#include<iostream>
#include<cstdio>
#include<vector>
#include<utility>
#include<algorithm>
#include<set>
#include<string>
#include<cstring>
#include<cmath>

using namespace std;

int main()

{
  
  freopen("out.txt", "w", stdout);
  int T,N,co=0;
  cin>>T;
  while((++co)<=T)
    {
      cin>>N;
      vector<string> s(N);
      vector<vector<int> > count(N);
      string sample,sample2;
      int i,j;
      int flag=1;
      for(i=0;i<N;i++)
	{
	  cin>>s[i];
	  sample2="";
	  sample2.push_back(s[i][0]);
	  count[i].push_back(1);
	  for(j=1;j<s[i].length();j++)
	    {
	      if(s[i][j]!=s[i][j-1])
		{
		  sample2.push_back(s[i][j]);
		  count[i].push_back(1);
		}
	      else
		{
		  count[i][count[i].size()-1]++;
		}
	    }
	  if(i==0)
	    {
	      sample=sample2;
	    }
	  else
	    {
	      if(sample.compare(sample2)!=0)
		{
		  flag=0;
		}
	    }

	}
      if(!flag)
	{
	  cout<<"Case #"<<co<<": Fegla Won"<<endl;
	}
      else
	{
	  int min=0,min1,k,cont;
	  for(i=0;i<sample.length();i++)
	    {
	      for(j=0;j<N;j++)
		{
		  cont=0;
		  for(k=0;k<N;k++)
		    {
		      if(k!=j)
			{
			  cont+=abs(count[j][i]-count[k][i]);
			}
		    }
		  if(j==0)
		    {
		      min1=cont;
		    }
		  else
		    {
		      if(min1>cont)
			{
			  min1=cont;
			}
		    }
		}
	      min+=min1;
	    }
	  cout<<"Case #"<<co<<": "<<min<<endl;
	} 
    }

  return 0;

}
