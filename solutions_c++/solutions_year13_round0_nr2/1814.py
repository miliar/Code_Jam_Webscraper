#include<iostream>
#include<stdio.h>

using namespace std;



int main()
{
int t=0;

scanf("%d",&t);
int t_=0;
int n=0,m=0;

int arr[100][100];
int final_arr[100][100];
int row_max[100];
int col_max[100];

while(t_<t)
{
	t_++;
	scanf("%d%d",&n,&m);

	for(int i=0;i<100;i++)
	{
		row_max[i]=0;
		col_max[i]=0;
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			{
				scanf("%d",&arr[i][j]);
				//cout<<arr[i][j]<<" ";
				if(row_max[i]<arr[i][j])row_max[i]=arr[i][j];
			}
			//cout<<endl;
	}

	for(int i=0;i<m;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(col_max[i]<arr[j][i])col_max[i]=arr[j][i];
		}
	}

	for(int i=0;i<n;i++)
	{
		//cout<<"row_max "<<i<<" "<<row_max[i]<<endl;
		for(int j=0;j<m;j++)
			final_arr[i][j]=row_max[i];
	}

	for(int i=0;i<m;i++)
	{
		//cout<<"col_max "<<i<<" "<<col_max[i]<<endl;		
		for(int j=0;j<n;j++)
		{
			if(final_arr[j][i]>col_max[i])final_arr[j][i]=col_max[i];
		}
	}

	int flag=1;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(arr[i][j]!=final_arr[i][j])
			{
				flag=0;break;
			}
		}
		if(flag==0)break;
	}
	if(flag==0)
		printf("Case #%d: NO\n",t_);
	else if(flag==1)
		printf("Case #%d: YES\n",t_);
	}
	return 0;
}
