#include<iostream>
using namespace std;

int arr1[5][5], arr2[5][5];
int ans1, ans2;

int main()
{
	freopen("d:\\1.txt", "r", stdin);
	freopen("d:\\1-out.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int kase = 1; kase <= T; ++kase)
	{
		cin>>ans1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin>>arr1[i][j];
		
		cin>>ans2;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin>>arr2[i][j];
				
		ans1--;ans2--;
		int ans, cnt = 0;
		
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(arr1[ans1][i] == arr2[ans2][j])
				{
					ans = arr1[ans1][i];
					cnt++;
				}
				
		cout<<"Case #"<<kase<<": ";
		if(cnt == 1)
		{
			cout<<ans<<endl;
		}
		else if(cnt == 0)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Bad magician!"<<endl;
		}
	}
	
	return 0;
}
