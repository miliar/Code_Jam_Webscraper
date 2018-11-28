#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		int N,M;
		cin>>N>>M;

		int lawn[110][110] = {0};
		for (int j = 0; j < N; ++j)
			for (int k = 0; k < M; ++k)
				cin>>lawn[j][k];

		bool possible = true;
		for (int j = 0; j < N; ++j)
		{
			for (int k = 0; k < M; ++k)
			{
				int val = lawn[j][k];

				bool row = true;
				bool col = true;
				// check row j
				for (int m = 0; m < M; ++m)
					if (lawn[j][m] > val)
					{
						row = false;
						break;
					}

				// check col k
				for (int m = 0; m < N; ++m)
					if (lawn[m][k] > val)
					{
						col = false;
						break;
					}

				possible = row | col;
				if (!possible) break;
			}

			if (!possible) break;
		}

		cout<<"Case #"<<i+1<<": ";
		if (possible)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
}