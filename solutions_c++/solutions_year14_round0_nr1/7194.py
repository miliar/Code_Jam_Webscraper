#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      int row;
      vector<int> chosen(20);
      for(int i=1;i<=2;i++)
	{
	  cin>>row;
	  for(int r=1;r<=4;r++)
	    {
	      for(int c=1;c<=4;c++)
		{
		  int v;
		  cin>>v;
		  if(r==row)
		    chosen[v]++;
		}
	    }
	}
      int cnt=0,ans;
      for(int i=1;i<=16;i++)
	{
	  if(chosen[i]==2)
	    {
	      cnt++;
	      ans=i;
	    }
	}
      cout<<"Case #"<<t<<": ";
      if(cnt==0)
	cout<<"Volunteer cheated!\n";
      else if(cnt==1)
	cout<<ans<<endl;
      else
	cout<<"Bad magician!\n";
    }
  return 0;
}
