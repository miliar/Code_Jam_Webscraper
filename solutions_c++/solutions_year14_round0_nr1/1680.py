/*	ashish1610	*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tcase=1;tcase<=t;++tcase)
	{
		int row1;
		cin>>row1;
		row1--;
		int ar[4][4];
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>ar[i][j];
		int row2;
		cin>>row2;
		row2--;
		int ar1[4][4];
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin>>ar1[i][j];
		int ans,cnt=0;
		for(int i=0;i<4;++i)
		{
			for(int j=0;j<4;++j)
			{
				if(ar[row1][i]==ar1[row2][j])
				{
					ans=ar[row1][i];
					cnt++;
					break;
				}
			}
		}
		if(cnt==0)
			cout<<"Case #"<<tcase<<": "<<"Volunteer cheated!\n";
		else if(cnt==1)
			cout<<"Case #"<<tcase<<": "<<ans<<endl;
		else
			cout<<"Case #"<<tcase<<": "<<"Bad magician!\n";
	}
	return 0;
}
