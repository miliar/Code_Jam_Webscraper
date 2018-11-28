#include <iostream>
#include <cstdlib>
#define N 4
#define M 10


using namespace std;

int main()
{
	int T;
	int x,y;
	int i,j,k;
	int a[M][M],b[M][M];
	int S;
	cin>>T;
	S=T;
	while(T--)
	{
		cin>>x;
		x--;
		for(i=0;i<N;i++)
		{
			for(j=0;j<N;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>y;
		y--;
		for(i=0;i<N;i++)
		{
			for(j=0;j<N;j++)
			{
				cin>>b[i][j];
			}
		}
		for(i=0;i<N;i++)
		{
			for(j=0;j<N;j++)
			{
				for(k=0;k<N;k++)
				{
					if(b[i][j]==a[x][k])
					{
						b[i][j]=-b[i][j];
						break;
					}
				}
			}
		}
		for(i=0,k=0,j=0;i<N;i++)
		{
			if(b[y][i]<0)
			{
				j=i;
				k++;
			}
		}
		cout<<"Case #"<<S-T<<": ";
		if(k==0)
			cout<<"Volunteer cheated!"<<endl;
		else if(k==1)
			cout<<-b[y][j]<<endl;
		else 
			cout<<"Bad magician!"<<endl;

	}

	return 0;
}

