// First.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for (int k = 0; k < T; ++k)
    {
        int n, m;
        bool can = true;
        cin >> n >> m;
        vector <vector <int> > lawn (n, vector <int> (m));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; j++)
                cin >> lawn [i][j];
        for (int i = 0; i < n; ++i)
        {
            int max = lawn [i][0];
            for (int j = 0; j < m; ++j)
            {
                if (lawn [i][j] > max)
                    max = lawn [i][j];
            }
            for (int j = 0; j < m; ++j)
            {
                if (lawn [i][j] < max)
                {
                    for (int l = 0; l < n; l++)
                    {
                        if (lawn [l][j] > lawn [i][j])
                            can = false;
                    }
                }
            }
        }
        for (int i = 0; i < m; ++i)
        {
            int max = lawn [0][i];
            for (int j = 0; j < n; ++j)
            {
                if (lawn [j][i] > max)
                    max = lawn [j][i];
            }
            for (int j = 0; j < n; ++j)
            {
                if (lawn [j][i] < max)
                {
                    for (int l = 0; l < m; l++)
                    {
                        if (lawn [j][l] > lawn [j][i])
                            can = false;
                    }
                }
            }
        }
        if (can)
            cout << "Case #" << k + 1 << ": YES" << endl;
        else
            cout << "Case #" << k + 1 << ": NO" << endl;
    }
	return 0;
}

