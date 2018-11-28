#include<iostream>
#include<string>
using namespace std;

int g[101][101];
int a[101],b[101];

int main()
{
	int T;
	cin>>T;
	for (int cas=1;cas<=T;cas++)
	{
		int n,m;
		cin>>n>>m;
		for (int i=0;i<n;i++)
			a[i]=0;
		for (int j=0;j<m;j++)
			b[j]=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
			{
				cin>>g[i][j];
				if (g[i][j]>a[i])
					a[i]=g[i][j];
				if (g[i][j]>b[j])
					b[j]=g[i][j];
			}
		string ret;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (g[i][j]<a[i]&&g[i][j]<b[j])
				{
					ret="NO";
					goto lab;
				}
		ret="YES";
lab:
		cout<<"Case #"<<cas<<": "<<ret<<endl;
	}
}
