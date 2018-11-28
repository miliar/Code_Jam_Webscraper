#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int A1[4][4];
	int T;
	cin>>T;
	for(int i=0; i<T;i++)
	{
		int n;
		cin>>n;
		int A1[4];
		int A2[4];
		for(int j=0;j<4;j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if(j+1==n)
				{
					cin>>A1[k];
				}				
				else
				{
					int x;
					cin>>x;
				}
			}
		}
		int m;
		cin>>m;

		for(int j=0;j<4;j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if(j+1==m)
				cin>>A2[k];
				else
				{
					int x;
					cin>>x;
				}
			}
		}
/*		cout<<m<<endl;
*/		int count = 0;
		int number = 0;
/*		for (int j = 0; j < 4; ++j)
		{
			cout<<A1[j]<<" ";
		}
		cout<<endl;
		for (int j = 0; j < 4; ++j)
		{
			cout<<A2[j]<<" ";
		}
		cout<<endl;
*/		for(int j = 0; j<4;j++)
		{
			for(int k = 0;k<4;k++)
			{
				if(A1[j] == A2[k])
				{
					count++;
					number = A1[j];
				}
			}
		}
		if(count == 0)
		{
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else if(count > 1)
		{
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<number<<endl;
		}


	}
	return 0;
}