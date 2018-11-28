#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		int arr1[4][4];
		int arr2[4][4];
		int c1,c2;
		cin>>c1;
		for(int l=0;l<4;++l)
		{
			for(int m=0;m<4;++m)
			{
				cin>>arr1[l][m];
			}
		}
		cin>>c2;
		for(int l=0;l<4;++l)
		{
			for(int m=0;m<4;++m)
			{
				cin>>arr2[l][m];
			}
		}
		set<int> fans;
		for(int l=0;l<4;++l)
		{
			fans.insert(arr1[c1-1][l]);
		}
		vector<int> ans;
		for(int l=0;l<4;++l)
		{
			if(fans.count(arr2[c2-1][l]) !=0 )
			{
				ans.push_back(arr2[c2-1][l]);
			}
		}
		cout<<"Case #"<<i<<": ";
		if(ans.size()>1){cout<<"Bad magician!\n";}
		else if(ans.size()==0){cout<<"Volunteer cheated!\n";}
		else{cout<<ans[0]<<endl;}
		
	}
	return 0;
}
