#include<bits/stdc++.h>
using namespace std;
int main()
{
	int T,i,p,q,j,t,a[4][4],b[4][4],count,ans;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>p;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		cin>>q;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		count =0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[p-1][i] == b[q-1][j])
				{
				    count++;
				    ans = i;
				}
			}
		}
		if(count == 1)
		{
			cout<<"Case #"<<t<<": "<<a[p-1][ans]<<endl;
		}
		else if(count > 1)
		{
			cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
		}
		else if(count==0)
		{
			cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
