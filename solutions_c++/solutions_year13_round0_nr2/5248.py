#include<iostream>
using namespace std;

int arr[110][110],rowmax[110],colmax[110];
int N=0,M=0;

void input()
{
	cin >> N >> M;
//	cout << "\n" << N << "\n" << M;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
			cin >> arr[i][j];
	}
}

void do_max()
{
	int max=0;
	for(int i=0;i<N;i++)
	{
		max=arr[i][0];
		for(int j=0;j<M;j++)
		{
			if(arr[i][j]>max)
				max=arr[i][j];
		}
		rowmax[i]=max;
	}		
	for(int i=0;i<M;i++)
	{
		max=arr[0][i];
		for(int j=0;j<N;j++)
		{
			if(arr[j][i]>max)
				max=arr[j][i];
		}
		colmax[i]=max;
	}
	/*cout << "\n";
	for(int i=0;i<N;i++)
		cout << rowmax[i] << "\t";
	cout << "\n";
	for(int i=0;i<M;i++)
		cout << colmax[i] << "\t";
*/
}

void operation()
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			if(arr[i][j] < rowmax[i] && arr[i][j] < colmax[j])
			{		
				cout << "NO\n";
				return;
			}
		}
	}
	cout << "YES\n";
}

int main()
{
	int T=0,i=1;
	cin >> T;
    	while(T--)
    	{
		input();
		do_max();
		cout << "Case #" << i << ": ";
		i++;
		operation();
    	}	
	return 0;
}
