#include <iostream>
#include <cstdio>
using namespace std;

int t;
int n, m;//row col
int a[101][101];//a[i,j]
bool r[101][101];//row
//bool c[101][101];//col

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int k, i, j, l;
	int maxv;
	bool jump;

	cin>>t;
	for (k=1; k<=t; k++)
	{
		jump = false;
		cin>>n>>m;
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++)
			{
				cin>>a[i][j];
				r[i][j] = false;//init
			}
		//row
		for (i=1; i<=n; i++)
		{
			maxv = 0;
			for (j=1; j<=m; j++)
				if (a[i][j]>maxv) maxv = a[i][j];
			for (j=1; j<=m; j++)
				r[i][j] = a[i][j]==maxv ? true:false;
		}
		//col
		for (j=1; j<=m; j++)
		{
			maxv = 0;
			for (i=1; i<=n; i++)
				if (a[i][j]>maxv) maxv = a[i][j];
			for (i=1; i<=n; i++)
				if (a[i][j]<maxv && r[i][j]==false)
				{
					jump = true;
					break;
				}
			if (jump == true)
				break;
		}
		if (jump == true)
			cout<<"Case #"<<k<<": NO"<<endl;
		else
			cout<<"Case #"<<k<<": YES"<<endl;
	}
	return 0;
}