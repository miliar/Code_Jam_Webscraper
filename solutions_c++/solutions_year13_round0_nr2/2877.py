#include <iostream>

using namespace std;

int main()
{
    int numCases;
    cin >> numCases;
    for (int caseNum = 1; caseNum <= numCases; caseNum++)
    {
	int N;
	cin >> N;
	int M;
	cin >> M;
	int ** lawn = new int*[N];
	for (int i = 0; i < N; i++)
	{
	    lawn[i] = new int[M];
	}
	for (int i = 0; i < N; i++)
	{
	    for (int j = 0; j < M; j++)
	    {
		cin >> lawn[i][j];
	    }
	}
	bool OK = true;
	for (int y = 0; y < N; y++)
	{
	    for (int x = 0; x < M; x++)
	    {
		bool horizontal = true;
		bool vertical = true;
		for (int i = 0; i < M; i++)
		{
		    if (lawn[y][i] > lawn[y][x])
		    {
			horizontal = false;
		    }
		}
		for (int j = 0; j < N; j++)
		{
		    if (lawn[j][x] > lawn[y][x])
		    {
			vertical = false;
		    }
		}
		OK = horizontal || vertical;
		if (!OK)
		{
		    break;
		}
	    }
	    if (!OK)
	    {
		break;
	    }
	}
	if (OK)
	{
	    cout << "Case #" << caseNum << ": YES" << endl;
	}
	else
	{
	    cout << "Case #" << caseNum << ": NO" << endl;
	}
    }
}
