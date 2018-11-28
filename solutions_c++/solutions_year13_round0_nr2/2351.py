#include<iostream>

using namespace std;

	
int T, M, N;
int arr[105][105];
bool check(int x, int y)
{
	bool f = true;
	for(int i = 0; i < N; ++i)
	{
		if(arr[i][y] > arr[x][y])
		{
			f = false;
			break;
		}
	}
	if(f == true)
		return true;
		
	f = true;
	for(int i = 0; i < M; ++i)
	{
		if(arr[x][i] > arr[x][y])
		{
			f = false;
			break;
		}
	}
	return f;
	
}
int main()
{
	freopen("F:\\download\\2.txt", "r", stdin);
	freopen("F:\\download\\2out.txt", "w", stdout);

	int id = 1;
	cin>>T;
	while(T--)
	{
		memset(arr, 0, sizeof(arr));
		cin>>N>>M;
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < M; ++j)
				cin>>arr[i][j];
		bool flag = true;
		for(int i = 0; i < N && flag; ++i)
			for(int j = 0; j < M; ++j)
			{
				if(check(i, j) == false)
				{
					flag = false;
					break;
				}
			}
		if(flag)
		{
			cout<<"Case #"<<id<<": YES"<<endl;
		}
		else
			cout<<"Case #"<<id<<": NO"<<endl;
		id++;
	}
	return 0;
}