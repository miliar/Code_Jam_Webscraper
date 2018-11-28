#include <iostream>
#include <vector>
#define N 4
using namespace std;

int main()
{
	int t;
	int choose;
	int count[N*N];
	int map[N][N];
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		for (int j=0;j<N*N;j++)
			count[j] = 0;
		for (int j=0;j<2;j++)
		{
			cin >> choose;
			for (int k=0;k<4;k++)
				for (int l=0;l<4;l++)
					cin >> map[k][l];
			for (int k=0;k<4;k++)
				count[map[choose-1][k]-1]++;
		}
		vector<int> ans;
		for (int j=0;j<N*N;j++)
			if (count[j]==2)
				ans.push_back(j);
		cout << "Case #" << i << ": ";
		if (ans.size()==1)
			cout << ans[0]+1;
		else if (ans.size()!=0)
			cout << "Bad magician!";
		else
			cout << "Volunteer cheated!";
		cout << endl;
	}
	return 0;
}
