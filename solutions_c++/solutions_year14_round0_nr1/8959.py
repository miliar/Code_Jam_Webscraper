#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		int first;
		cin>>first;

		int arrange1[4][4];
		for (int j = 0; j < 4; ++j)
			for (int k = 0; k < 4; ++k)
			{
				int tmp;
				cin>>tmp;
				arrange1[j][k] = tmp;
			}

		int second;
		cin>>second;

		int arrange2[4][4];
		for (int j = 0; j < 4; ++j)
			for (int k = 0; k < 4; ++k)
			{
				int tmp;
				cin>>tmp;
				arrange2[j][k] = tmp;
			}

		int cnt = 0;
		int idx = -1;
		for (int j = 0; j < 4; ++j)
		{
			int answer = arrange1[first-1][j];
			for (int k = 0; k < 4; ++k)
				if (answer == arrange2[second-1][k])
				{
					++cnt;
					idx = j;
				}
		}

		cout<<"Case #"<<i+1<<": ";
		if (cnt == 1)
			cout<<arrange1[first-1][idx];
		else if (cnt > 1)
			cout<<"Bad magician!";
		else
			cout<<"Volunteer cheated!";
		cout<<endl;
	}
}