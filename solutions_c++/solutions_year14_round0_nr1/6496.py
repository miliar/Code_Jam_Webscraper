#include<iostream>
using namespace std;

int main()
{
  int t;
  int casenum = 0;

  cin>>t;

  while(t--)
    {
      int nn[17] = {0};
      int m[4][4];
      int r1,r2;

      casenum++;

      cin>>r1;

      for(int i = 0;i<4;i++)
	for(int j = 0;j<4;j++)
	  {
	    cin>>m[i][j];
	  }

      for(int i =0;i<4;i++)
	{
	  nn[m[r1-1][i]]++;
	}

      cin>>r2;
      for(int i = 0;i<4;i++)
	for(int j = 0;j<4;j++)
	  {
	    cin>>m[i][j];
	  }

      for(int i =0;i<4;i++)
	{
	  nn[m[r2-1][i]]++;
	}

      int num2=0;
      int ans = -1;

      for(int i = 1;i<17;i++)
	{
	  if(nn[i]==2)
	    {
	    num2++;
	    ans = i;
	    }
	}

      cout<<"Case #"<<casenum<<": ";

      if(num2==1)
	{
	  cout<<ans<<endl;
	}
      else if(num2==0)
	{
	  //volun cheated
	  cout<<"Volunteer cheated!\n";
	}
      else 
	{
	  cout<<"Bad magician!\n";
	}      
    }

  return 0;
}
