#include<iostream>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int t,n,m,te,a1,a2,r1[5][5],r2[5][5],i,j;
	cin>>t;
	for(te=1;te<=t;te++){
		cin>>a1;
		a1--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>r1[i][j];
		cin>>a2;
		a2--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>r2[i][j];
		int tak[25]={0};
		for(i=0;i<4;i++)
			tak[r1[a1][i]]=1;
		int ans=-1;
		cout<<"Case #"<<te<<": ";
		for(i=0;i<4;i++)
			if (tak[r2[a2][i]]==1)
				if (ans==-1)
					ans=r2[a2][i];
				else
				{
					ans=-2;
					break;
				}
		if(ans==-2)
			cout<<"Bad magician!\n";
		else if(ans==-1)
			cout<<"Volunteer cheated!\n";
		else
			cout<<ans<<"\n";
	}
	return 0;
}
