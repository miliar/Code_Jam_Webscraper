#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int test,x,m,i,j,k,maxno,n,flag;
	int count[200][200],dp[200][200];
	cin>>test;
	for(int curr=1;curr<=test;curr++)
	{

		cin>>n>>m;

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin>>count[i][j];

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				dp[i][j]=-1;

		flag=1;

		for(i=0;i<n;i++)
		{
			maxno=0;

			for(j=0;j<m;j++)
				maxno=max(count[i][j],maxno);


			for(j=0;j<m;j++)
			{
				if(dp[i][j]==-1)
				{
					if(maxno!=count[i][j])
					{
						for(k=0;k<n;k++)
						{
							if(dp[k][j]==-1)
							{
								dp[k][j]=count[i][j];
							}
							else if(dp[k][j]!=count[i][j])
								flag=0;
						}
					}

					else
						dp[i][j]=count[i][j];
				}
				else
					if(dp[i][j]!=count[i][j])
						flag=0;
			}
		}
		cout<<"Case #"<<curr<<": ";
		if(flag)
			cout<<"YES";
		else
			cout<<"NO";
		cout<<"\n";
	}
	return 0;
}
