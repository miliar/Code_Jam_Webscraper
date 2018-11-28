#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
	int n;
	cin>>n;
	for(int T=1;T<=n;T++)
	{
		int choice[2];
		vector<vector<vector<int> >> arrangement(2,vector<vector<int>>(4,vector<int>(4,0)));
		vector<int> joined;
		for(int x=0;x<2;x++)
		{
			cin>>choice[x];
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
					cin>>arrangement[x][i][j];
			}
			sort(arrangement[x][choice[x]-1].begin(),arrangement[x][choice[x]-1].end());
		}
		joined.resize(4);
		set_intersection(arrangement[0][choice[0]-1].begin(),arrangement[0][choice[0]-1].end(),
						arrangement[1][choice[1]-1].begin(),arrangement[1][choice[1]-1].end()
						,joined.begin());
		cout<< "Case #"<<T<<": ";
		if(joined[0] == 0)
		{
			cout<<"Volunteer cheated!";
		}
		else if(joined[0] != 0 && joined[1] != 0)
		{
			cout<<"Bad magician!";
		}
		else
		{
			cout<<joined[0];
		}
		cout<<endl;
	}
	return 0;
}