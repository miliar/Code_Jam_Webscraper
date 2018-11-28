#include<iostream>

using namespace std;

int main()	{
  int tc;
  cin>>tc;
  for(int t=0;t<tc;t++)	{
    int n,m;
    cin>>n>>m;
    
    int mat[n][m];
    int dup[n][m];
    int max[n];
    int i,j,k,flag=0;
    
    //main mat
    for(i=0;i<n;i++)	{
      for(j=0;j<m;j++)	{
	cin>>mat[i][j];
      }
    }
    
    for(i=0;i<n;i++)	{
      max[i]=0;
    }

    for(i=0;i<n;i++)	{
      for(j=0;j<m;j++)	{
	if(max[i]<mat[i][j])	{
	  max[i]=mat[i][j];
	  for(k=0;k<m;k++)	{
	    dup[i][k]=max[i];
	  }
	}
      }
    }
    for(i=0;i<n;i++)	{
      for(j=0;j<m;j++)	{
	if(mat[i][j]<max[i])	{
	  for(k=0;k<n;k++)	{
	    dup[k][j]=mat[i][j];
	  }
	}
      }
    }
    for(i=0;i<n;i++)	{
      for(j=0;j<m;j++)	{
	if(dup[i][j] != mat[i][j])	{
	  cout<<"Case #"<<t+1<<": NO"<<endl;
	  flag=1;
	  break;
	}
      }
	if(flag==1)	{
	  break;
	}
      
    }
    if(flag==0)	{
      cout<<"Case #"<<t+1<<": YES"<<endl;
    }
  }
  return 0;
}