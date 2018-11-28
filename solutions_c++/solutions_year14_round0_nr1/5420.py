#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin>>T;
	int k=0;
	while(T--)
	{
		if(k)
		cout<<endl;
		k++;
		cout<<"Case #"<<k<<": ";
		int row1,row2;
		cin>>row1;
		row1--;
		int arr1[4][4];
		int arr2[4][4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr1[i][j];
		cin>>row2;
		row2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr2[i][j];
		set<int> s;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr1[row1][i]==arr2[row2][j])
					s.insert(arr1[row1][i]);
			}
		}
		if(s.size()==0)
		{
			cout<<"Volunteer cheated!";
			continue;
		}
		if(s.size()==1)
		{
			set<int>::iterator it=s.begin();
			cout<<(*it);
			continue;
		}
		cout<<"Bad magician!";
	}
}
