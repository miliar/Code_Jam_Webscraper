#include <bits/stdc++.h>

using namespace std;

int main()
{
  freopen("in2.in","r",stdin);
  freopen("out2.out","w",stdout);
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
	 
	  int r1,r2;
	  int g1[5][5];
	  int g2[5][5];
	  cin>>r1;
	  for(int i=1;i<=4;i++)
	  {
		  for(int j=1;j<=4;j++)
		  {
			  cin>>g1[i][j];
		  }
	  }
	  cin>>r2;
	  for(int i=1;i<=4;i++)
	  {
		  for(int j=1;j<=4;j++)
		  {
			  cin>>g2[i][j];
		  }
	  }
	  int matches = 0;
	  int ans ;
	  for(int i=1;i<=4;i++)
	  {
		  int x=g1[r1][i];
		  for(int j=1;j<=4;j++)
		  {
			   int y =g2[r2][j];
			   if(x==y)
			   {
				   matches++;
				   ans = g2[r2][j];  
			   }
		  }
	  }
	  
	  cout<<"Case #"<<t<<": ";
	  switch(matches)
	  {
		  case 0 :cout<<"Volunteer cheated!"; break;
		  case 1 :cout<<ans;break;
		  default :cout<<"Bad magician!";break;
	  }
	  cout<<'\n';
	  
	  
  }	
  return 0;
}
