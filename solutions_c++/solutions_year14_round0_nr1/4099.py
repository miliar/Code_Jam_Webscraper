#include <iostream>

using namespace std;
int main()
{
	int t,c1,c2,ctr,n;
	int a[4][4],b[4][4];
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cin >> c1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin >> a[j][k];
			} 
		}
		cin >> c2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin >> b[j][k];
			}
		}
		ctr=0;n=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[c1-1][j]==b[c2-1][k])
				{
					ctr++;
					n=a[c1-1][j];
				}
			}
		}
		cout << "Case #" << i << ": ";
		if(ctr>1)
		{
			cout << "Bad magician!";
		}
		else if(ctr==1)
		{
			cout << n;
		}
		else
		{
			cout << "Volunteer cheated!";
		}
		cout << "\n";
	}
	return 0;
}
