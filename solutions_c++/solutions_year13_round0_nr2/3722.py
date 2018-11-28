#include <iostream>
using namespace std;

int row[110];
int col[110];
int a[110][110];

int main()
{
	int z,t,i,j,n,m;
	bool flag;
	cin >> t;
	for(z=1;z<=t;z++)
	{
		cin >> n >> m;
		for(i=1;i<=n;i++)
		{
			row[i]=0;
			for(j=1;j<=m;j++)
			{
				cin >> a[i][j];
				row[i]=max(row[i],a[i][j]);
			}
		}
		for(i=1;i<=m;i++)
		{
			col[i]=0;
			for(j=1;j<=n;j++)
				col[i]=max(col[i],a[j][i]);
		}
		flag=1;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				if(a[i][j]!=row[i]&&a[i][j]!=col[j])
				{
					flag=0;
					break;
				}
		if(flag)
			cout << "Case #" << z << ": YES" << endl;
		else
			cout << "Case #" << z << ": NO" << endl;
	}
	return 0;
}
					
