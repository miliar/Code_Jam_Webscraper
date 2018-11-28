#include <iostream>

using namespace std;

int main()
{
    int n, m, t;
    short map[100][100];
    bool bmap[100][100];

    cin >> t;
    for (int i = 0; i < t; ++i)
    {
	cout << "Case #" << i+1 << ": ";

	cin >> n >> m;
	for (int j = 0; j < n; ++j)
	{
	    int row_max = 0;
	    for (int k = 0; k < m; ++k)
	    {
		cin >> map[j][k];
		if (map[j][k] > row_max) row_max = map[j][k];
		bmap[j][k] = false;
	    }
	    for (int k = 0; k < m; ++k)
	    {
		if (map[j][k] == row_max)
		    bmap[j][k] = true;
	    }
	}

	// Columns
	for (int j = 0; j < m; ++j)
	{
	    int col_max = 0;
	    for (int k = 0; k < n; ++k)
	    {
		if (map[k][j] > col_max) col_max = map[k][j];
	    }
	    for (int k = 0; k < n; ++k)
	    {
		if (map[k][j] == col_max) bmap[k][j] = true;
	    }
	    //cout << "col_max " << j << ": " << col_max;
	}

	// Check
	bool done = false;
	bool ans = true;
	for (int j = 0; j < n; ++j)
	{
	    for (int k = 0; k < m; ++k)
	    {
		if (bmap[j][k] == false)
		{
		    done = true;
		    ans = false;
		    break;
		}
	    }
	    if (done)
		break;
	}

	if (ans)
	{
	    cout << "YES" << endl;
	}
	else
	{
	    cout << "NO" << endl;
	}
    }

}
