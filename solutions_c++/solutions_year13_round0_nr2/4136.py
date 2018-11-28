#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math>
#include <algorithm>

using namespace std;

bool check(vector<vector<int> > grid, int x, int y)
{
    bool flag = true;

    for(int i = 0; i < grid[x].size(); i++)
    {
        if(grid[x][i] > grid[x][y])
        {
            flag = false;
            break;
        }
    }
    if(flag)
        return true;

    for(int i = 0; i < grid.size(); i++)
        if(grid[i][y] > grid[x][y])
            return false;
    return true;
}

int main()
{
    ofstream out("lawn.out");
    ifstream in("lawn.in");

    int T, temp,N,M;
    in >> T;

    for(int i = 0; i < T; i++)
    {
        in >> N >> M;
        vector<vector<int> > grid(N);
        for(int j=0; j<N; j++)
        {
            for(int k=0; k<M; k++)
            {
                in >> temp;
                grid[j].push_back(temp);
            }
        }

        bool flag = 0;

        for(int j = 0; j < N; j++)
        {
            for(int k = 0; k < M; k++)
            {
                if(!check(grid,j,k))
                {
                    out << "Case #" << i+1 << ": NO" << endl;
                    flag = 1;
                    break;
                }
            }
            if(flag) break;
        }
        if(flag) continue;
        else
            out << "Case #" << i+1 << ": YES" << endl;

    }

    return 0;
}

