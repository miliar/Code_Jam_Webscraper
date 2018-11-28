#include<iostream>
using namespace std;
int main()
{
	int t,ans1,ans2;
	int mat1[4][4],mat2[4][4];
	freopen("input.in","r",stdin);
	freopen("output1.txt","w",stdout);
	
	cin>>t;
	for(int k=1;k<=t;k++)
	{
	  int count=0;
	  int result=0;
	  cin>>ans1;
	  for(int i=0;i<4;i++)
	  {
		for(int j=0;j<4;j++)
		{
			cin>>mat1[i][j];
		}
	  }  
     
	  cin>>ans2;
	  for(int i=0;i<4;i++)
	  {
		for(int j=0;j<4;j++)
		{
			cin>>mat2[i][j];
		}
      }
	  
	  for(int i=0;i<4;i++)
	  {
	  	for(int j=0;j<4;j++)
	  	{
	  		if(mat1[ans1-1][i]==mat2[ans2-1][j])
	  		{
	  		    result=mat1[ans1-1][i];
	  		    count++;
	  		    break;
	  		}
	  	}
	  }  
	  
	  if(count==0)
	  {
	  	cout<<"Case #"<<k<<": "<<"Volunteer cheated!";
	  }
	  else if(count==1)
	  {
	  	cout<<"Case #"<<k<<": "<<result;
	  }
	  else
	  {
	  	cout<<"Case #"<<k<<": "<<"Bad magician!";
	  }
	  cout<<"\n";
  }
	return 0;
}
