#include<iostream>
using namespace std;

int main()
{
	int a[4][4],b[4][4];
	int tc;
	int m,n;
	cin>>tc;
	for(int q = 1;q<=tc;q++)
	{
		cin>>m;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>n;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		m = m-1;
		n = n-1;
		int count = 0;
		int number;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				if(a[m][i] == b[n][j])
				{
					count++;
					if(count<=1)
						number = a[m][i];
				}
			}
		}
		if(count == 1)
		{
			cout<<"Case #"<<q<<": "<<number<<endl;
		}
		if(count > 1)
		{
			cout<<"Case #"<<q<<": Bad magician!"<<endl;
		}
		if(count == 0)
		{
			cout<<"Case #"<<q<<": Volunteer cheated!"<<endl;
		}
	}
}
