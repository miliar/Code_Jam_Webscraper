#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t,up=1;
	cin>>t;
	while(t--)
	{
		int first,second,a[4][4],b[4][4],ans,cnt=0;
		cin>>first;
		first-=1;
		for(int i = 0 ;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>a[i][j];
		cin>>second;
		second-=1;
		for(int i = 0 ;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>b[i][j];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[first][i]==b[second][j])
				{
					cnt++;
					ans=a[first][i];
				}
		cout<<"Case #"<<up<<": ";
		if(cnt==0)
			cout<<"Volunteer cheated!"<<endl;
		else if(cnt==1)
			cout<<ans<<endl;
		else if(cnt>1)
			cout<<"Bad magician!"<<endl;
		up++;
	}
	return 0;
}
