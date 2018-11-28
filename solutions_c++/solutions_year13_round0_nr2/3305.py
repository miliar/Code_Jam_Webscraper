#include <iostream>
#include <set>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	for(int n=1; n<=cases; n++)
	{
		int grass[100][100];
		int N, M;
		cin >> N >> M;

		int maxX[100];
		int maxY[100];

		for(int i=0; i<N; i++)
		{
			maxX[i] = 0;
			for(int j=0; j<M; j++)
			{
				if(i==0)
					maxY[j] = 0;

				cin >> grass[i][j];
				if(grass[i][j] > maxX[i])
					maxX[i] = grass[i][j];
				if(grass[i][j] > maxY[j])
					maxY[j] = grass[i][j];
			}
		}

		bool possible = true;
		for(int i=0; i<N && possible; i++)
		{
			for(int j=0; j<M && possible; j++)
			{
				if(grass[i][j] != maxX[i] && grass[i][j] != maxY[j])
					possible = false;
			}
		}

		cout << "Case #" << n << ": ";
		if(possible)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}
