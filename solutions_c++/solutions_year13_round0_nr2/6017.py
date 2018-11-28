#include <iostream>
#include <vector>
using namespace std;

bool check(int arr[100][100],int rows,int columns)
{
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<columns;j++)
		{
			if(arr[i][j]==1)
			{
				bool flag= true;
				for(int a=0;a<columns;a++)
				{
					if(arr[i][a]!=1)
						flag=false;
				}

				if(!flag)
				{
					for(int a=0;a<rows;a++)
					{
						if(arr[a][j]!=1)
							return false;
					}
				}
			}

		}
	}

	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int arr[100][100] ; 
	int rows,columns;
	int testcases;
	cin>>testcases;
	for(int t=1;t<=testcases;t++)
	{
		cin>>rows>>columns;
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<columns;j++)
			{
				cin>>arr[i][j];
			}
		}
		if(check(arr,rows,columns))
			cout<<"Case #"<<t<<": "<<"YES"<<endl;
		else
			cout<<"Case #"<<t<<": "<<"NO"<<endl;
	}

	return 0;
}