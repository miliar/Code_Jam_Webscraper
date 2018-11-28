#include <vector>
#include <iostream>

using namespace std;

bool canCut(int x, int y, vector <vector <int> > & lawn)
{
	bool canCutx = true;
	bool canCuty = true;
	for (int i=0; i<lawn.size(); i++)
	{
		if(lawn[i][y]>lawn[x][y])
		{
			canCutx = false;
			break;
		}
	}
	
	for (int i=0; i<lawn[x].size(); i++)
	{
		if (lawn[x][i]>lawn[x][y])
		{
			canCuty = false;
			break;
		}
	}
	
	if (!canCutx && !canCuty)
		return false;
	return true;
}

int main()
{
	int T;
	cin >> T;
	
	for (int i=0; i<T; i++)
	{
		int N, M;
		cin >> N >> M;
		
		vector <vector <int> > lawn(N, vector <int> (M));
		for (int j=0; j<N; j++)
			for (int k=0; k<M; k++)
				cin >> lawn[j][k];
		
		bool isPossible = true;
		for (int j=0; j<N; j++)
		{
			for (int k=0; k<M; k++)
			{
				if (!canCut(j, k, lawn))
					isPossible = false;
			}
			if (!isPossible)
				break;
		}
		
		cout << "Case #" << i+1 << ": ";
		if (isPossible)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}