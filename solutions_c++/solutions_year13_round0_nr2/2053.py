#include <iostream>
#define N 105
using namespace std;
int tr[N][N];
int kol[N];
int wie[N];
int main()
{
	ios_base::sync_with_stdio(0);
	int test;
	cin>>test;
	for(int y=1; y<=test; y++)
	{
		cout<<"Case #"<<y<<": ";
		int n, m;
		cin>>n>>m;
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=m; j++)
			{
				kol[j]=0;
				wie[i]=0;
				cin>>tr[i][j];
			}
		}
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=m; j++)
			{
				kol[j]=max(kol[j], tr[i][j]);
				wie[i]=max(wie[i], tr[i][j]);
			}
		}
		bool odp=true;
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=m; j++)
			{
				if(tr[i][j]!=kol[j] && tr[i][j]!=wie[i])
				{
					odp=false;
				}
			}
		}
		if(odp)
		{
			cout<<"YES"<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
	return 0;
}
