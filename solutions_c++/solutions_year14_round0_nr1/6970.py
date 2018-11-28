#include<iostream>

using namespace std;

int t,a,b,A[17],cnt,ans,temp1;

int main()
{
  cin>>t;
  
  for(int q=1;q<=t;q++)
  {
    for(int i=1;i<=16;i++)
      A[i]=0;
    cin>>a;
    for(int i=1;i<=4;i++)
    {
      for(int j=1;j<=4;j++)
      {
	cin>>temp1;
	if(i==a)
	  A[temp1]++;
      }
    }
    
    cin>>b;
    cnt=0;
    for(int i=1;i<=4;i++)
    {
      for(int j=1;j<=4;j++)
      {
	cin>>temp1;
	if(i==b)
	{
	  if(A[temp1])
	  {
	    cnt++;
	    ans=temp1;
	  }
	}
      }
    }
    
    cout<<"Case #"<<q<<": ";
    
    if(cnt==1)
      cout<<ans;
    else if(cnt==0)
      cout<<"Volunteer cheated!";
    else
      cout<<"Bad magician!";
    cout<<"\n";
  }
}
    
    