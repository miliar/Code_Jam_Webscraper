#include<iostream>
#include<algorithm>

using namespace std;

int t,n,m,A[101][101],C[101],R[101],flag1;

int main()
{
  cin>>t;
  
  for(int q=1;q<=t;q++)
  {
    cin>>n>>m;
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=m;j++)
	cin>>A[i][j];
    }
    
    for(int i=1;i<=n;i++)
    {
      int temp1=A[i][1];
      for(int j=1;j<=m;j++)
	temp1=max(temp1,A[i][j]);
      R[i]=temp1;
    }
    
    for(int i=1;i<=m;i++)
    {
      int temp1=A[1][i];
      for(int j=1;j<=n;j++)
	temp1=max(temp1,A[j][i]);
      C[i]=temp1;
    }
    
    flag1 =1;
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=m;j++)
      {
	if(R[i]==A[i][j])
	  continue;
	if(C[j]==A[i][j])
	  continue;
	flag1=0;
	break;
      }
      if(flag1==0)
	break;
    }
    
    cout<<"Case #"<<q<<": ";
    
    if(flag1==1)
      cout<<"YES\n";
    else
      cout<<"NO\n";
  }
}
	