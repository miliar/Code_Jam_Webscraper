#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t=0,r1=0,r2=0;
	cin>>t;
	int n=t;
	while(t--)
	{
		int a[4][4],b[4][4];
		cin>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		cin>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		int c,count=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[r1-1][i]==b[r2-1][j])
				{
					c=i;
					count++;
				}
			}
		}
		if(count==1)
			cout<<"Case #"<<n-t<<": "<<a[r1-1][c]<<endl;
		else if(count>=2)
			cout<<"Case #"<<n-t<<": Bad magician!"<<endl;
		else if(count==0)
			cout<<"Case #"<<n-t<<": Volunteer cheated!"<<endl;
	}
	return 0;
}