#include<iostream>

using namespace std;

int main()
{
	int test;
	cin>>test;
	for(int k =1; k <= test; k++)
	{
		int n,m;
		cin>>n>>m;
		int arr[n][m];
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
				cin>>arr[i][j];
		}
		while(true)
		{
			int min = 999;
			int row= -1,col = -1;
			int temp = 0;
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < m; j++)
				{
					if(arr[i][j] != 999)
						temp = 1;
				}
			}
			if(temp == 0)
			{
				cout<<"Case #"<<k<<": YES"<<endl;
				break;
			}
			int check = 0;
			if(temp == 1)
			{
				int del=0;
				for(int i = 0; i < n; i++)
				{
					for(int j = 0; j < m; j++)
					{
						if(arr[i][j] < min)
						{
							min = arr[i][j];
							row = i;
							col = j;	
						}
					}
				}
				for(int j = 0; j < m;j++)
				{
					if(arr[row][j] != min && arr[row][j] != 999)
					{
						del = 1;
						break;
					}
				}
				if(del == 0)
				{
					for(int j = 0; j < m;j++)
					{
						arr[row][j] = 999;
					}
					check = 1;
					del = -1;
				}
				if(del == 1)
				{
					del = 2;
					for(int i = 0; i <n; i++)
					{
						if(arr[i][col] != min && arr[i][col] != 999)
						{
							del = 0;
							break;
						}
					}
				}
				if(del == 2)
				{
					for(int i = 0; i <n; i++)
					{
						arr[i][col] = 999;
					}
					check = 1;
				}
			}
			if(temp == 1 && check == 0)
			{
				cout<<"Case #"<<k<<": NO"<<endl;
				break;
			}
		}
	}
	return 0;
}
