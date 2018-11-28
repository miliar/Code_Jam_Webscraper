#include<iostream>
using namespace std;
int main()
{
	int t,index,i,j,row,column,tag;
	int value[101][101];
	int row_max[101];
	int column_max[101];
	cin>>t;
	
	for(index=1;index<=t;index++)
	{
		cin>>row>>column;
		tag=0;
		for(j=1;j<=column;j++)
		{
			column_max[j]=0;
		}
		for(i=1;i<=row;i++)
		{
			row_max[i]=0;
			for(j=1;j<=column;j++)
			{
				cin>>value[i][j];
				if(value[i][j]>row_max[i])
				{
					row_max[i]=value[i][j];
				}
				if(value[i][j]>column_max[j])
				{
					column_max[j]=value[i][j];
				}
			}
		}
		for(i=1;i<=row;i++)
		{
			for(j=1;j<=column;j++)
			{
				if(value[i][j]>=row_max[i] || value[i][j]>=column_max[j])
				{
					continue;
				}
				else
				{
					tag=1;
					break;	
				}
			}
			if(tag==1)
			{
				break;
			}
		}
		cout<<"Case #"<<index<<": ";
		if(tag==1)
		{	
			cout<<"NO";
		}
		else if(tag==0)
		{
			cout<<"YES";
		}
		cout<<endl;
	}
}
