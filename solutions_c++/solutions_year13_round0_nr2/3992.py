#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin>>T;

	for (int t = 0; t < T; ++t)
	{
		int N,M;
		cin>>N>>M;

		int cell[100][100];
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				cin>>cell[i][j];
			}
		}

		bool find = false;
		for (int i = 0; i < N; ++i)
		{
			if(find)
				break;
			for (int j = 0; j < M; ++j)
			{
				if (find)
				{
					break;
				}

				bool row = false;
				bool col = false;
				int a = cell[i][j];

				for (int r = 0; r < M; ++r)
				{
					if (cell[i][r] > a)
					{
						row = true;
						break;
					}
				}
				for (int r = 0; r < N; ++r)
				{
					if (cell[r][j] > a)
					{
						col = true;
						break;
					}
				}

				if (row && col)
				{
					find = true;
				}
			}
		}

		cout<<"Case #"<<t+1<<": ";
		if(find){
			cout<<"NO"<<endl;
		} else{
			cout<<"YES"<<endl;
		}
	}
	return 0;
}