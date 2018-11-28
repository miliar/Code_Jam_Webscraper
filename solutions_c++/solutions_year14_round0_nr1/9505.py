#include <iostream>
using namespace std;
int main()
{
	int N;
	cin>>N;

	int x[4][4],y[4][4],a,b,ctr=0,u=0;
	for(int i=0;i<N;i++)
	{
		cin>>a;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>x[j][k];
			}
		}
		cin>>b;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>y[j][k];
			}
		}
		ctr=0; u=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(x[a-1][j]==y[b-1][k])
				{
					ctr++;
					u=x[a-1][j];
				}
			}
		}
		if(ctr==0)
		{
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else if(ctr==1)
		{
			cout<<"Case #"<<i+1<<": "<<u<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
	}
}
