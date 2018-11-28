#include <iostream>
#include <vector>

using namespace std;

    int T;

void ucitajTravu(int n, int m, vector<vector<int> > &trava)
{
    for(int i = 0; i < n; i++)
    {
        vector<int> redTrave;
        for(int j = 0; j < m; j++)
        {
            int temp;
            cin >> temp;

            redTrave.push_back(temp);
        }

        trava.push_back(redTrave);
    }
}

bool imaVece(int n, int m, vector<vector<int> > &trava)
{
    bool stupac = false;

    for(int i = 0; i < trava.size(); i++)
    {
        if(trava[i][m] > trava[n][m])
        {
            stupac = true;
        }
    }

    if(!stupac)
    {
        return false;
    }

    for(int i = 0; i < trava[n].size(); i++)
    {
        if(trava[n][i] > trava[n][m])
        {
            return true;
        }
    }

    return false;
}

void pokosiTravu(int y, int n, int m, vector<vector<int> > &trava)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if(imaVece(i, j, trava))
            {
                cout << "Case #" << y+1 << ": NO\n";
                return;
            }
        }
    }

    cout << "Case #" << y+1 << ": YES\n";
}

int main()
{
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        int N, M;

        cin >> N >> M;

        vector<vector<int> > trava;

        ucitajTravu(N, M, trava);

        pokosiTravu(i, N, M, trava);
    }

    return 0;
}
