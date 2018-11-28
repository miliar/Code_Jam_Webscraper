#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<set>
#include<cstdio>
using namespace std;
//pandey
int main()
{
	//ios_base::sync_with_stdio(false);
	freopen("A-small.txt","r",stdin);
	freopen("A-ans-out.txt","w",stdout);
	
	int t;
	cin>>t;
	
	int count=1;
	
	while(t-->0)
	{
		int first,second;
		cin>>first;
		int af[4][4],as[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>af[i][j];
			}

		}
		cin>>second;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>as[i][j];
			}

		}
		int cards=0;
		int ans;
		first--;
		second--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(af[first][i]==as[second][j])
				{
					cards++;
					ans=af[first][i];
				}
			}
		}

		cout<<"Case #"<<count<<": ";

		if(cards==0)
		{
			cout<<"Volunteer cheated!";
		}
		else if(cards==1)
		{
			cout<<ans;
		}
		else if(cards>1)
		{
			cout<<"Bad magician!";
		}
		cout<<endl;
		count++;
	}
 
 
 
 
}
