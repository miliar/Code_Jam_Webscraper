#include <iostream>
using namespace std;

void check(int a[100][100],int m,int n)
{
	for(int i=0;i<m;i++)
	for(int j=0;j<n;j++)
	{
		bool t=true,l=true;
		for(int k=0;k<m;k++)
		{
			if(a[k][j]>a[i][j])
			{
				t=false;
				break;
			}
		}
		for(int k=0;k<n;k++)
		{
			if(a[i][k]>a[i][j])
			{
				l=false;
				break;
			}
		}
		if(!(t||l))
		{
			cout<<"NO"<<endl;
			return;
		}		
	}
	cout<<"YES"<<endl;
			return;
	
}
int main()
{
	int n;
	cin>>n;
	int k,m;
	for(int i=1;i<=n;i++)
	{
		cin>>k>>m;
		int a[100][100];
		for(int x=0;x<k;x++)
		for(int y=0;y<m;y++)
		cin>>a[x][y];
		cout<<"Case #"<<i<<": ";
		check(a,k,m);
	}
}
