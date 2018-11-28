#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for (int q=0;q<t;q++)
	{
		int fa;
		cin>>fa;
		int a[4][4],b[4][4];
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
			cin>>a[i][j];
		int fb;
		cin>>fb;
		for (int i=0;i<4;i++)
                        for (int j=0;j<4;j++)
                        cin>>b[i][j];
		int count=0;
		int k[4],l=0;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				if (a[fa-1][i]==b[fb-1][j])
				{
					k[count++]=a[fa-1][i];
				}
			}
		}
		if (count==0)
		cout<<"Case #"<<q+1<<": "<<"Volunteer cheated!";
		else if (count==1)
		cout<<"Case #"<<q+1<<": "<<k[count-1];
		else
		cout<<"Case #"<<q+1<<": "<<"Bad magician!";
		cout<<endl;
	}
}
