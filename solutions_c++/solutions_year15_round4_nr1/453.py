#include <iostream>
#include <vector>

using namespace std;

int allX[] = {-1, 0, 1, 0};
int allY[] = {0, -1, 0, 1};

int ySize, xSize;

bool HasArrow(const vector<string> &grid, int x, int y, int xChange, int yChange)
{
    x += xChange;
    y += yChange;
    
    for (;x >= 0 && x < xSize && y >= 0 && y < ySize; x += xChange, y += yChange)
    {
        if (grid[y][x] != '.')
            return true;
    }
    return false;
}

int GetCost(const vector<string> &grid, int x, int y, bool &valid)
{
    int initialChangeX, initialChangeY;
    switch (grid[y][x])
    {
    case '<':
        initialChangeX = -1;
        initialChangeY = 0;
        break;
    case '^':
        initialChangeX = 0;
        initialChangeY = -1;
        break;
    case '>':
        initialChangeX = 1;
        initialChangeY = 0;
        break;
    case 'v':
        initialChangeX = 0;
        initialChangeY = 1;
        break;
    }
    if (HasArrow(grid, x, y, initialChangeX, initialChangeY))
        return 0;
    for (int i = 0; i < 4; ++i)
        if (HasArrow(grid, x, y, allX[i], allY[i]))
            return 1;
    
    valid = false;
    return 0;
}

int main()
{
    int T;
    cin >> T;
    
    vector<string> grid;
    
    for (int t = 1; t <= T; ++t)
    {
        cin >> ySize >> xSize;
        grid.resize(ySize);
        
        for (int i = 0; i < ySize; ++i)
            cin >> grid[i];
        
        int cost = 0;
        bool valid = true;
        for (int y = 0; y < ySize; ++y)
        {
            for (int x = 0; x < xSize; ++x)
            {
                if (grid[y][x] != '.')
                {
                    cost += GetCost(grid, x, y, valid);
                }
            }
        }
        
        cout << "Case #" << t << ": ";
        if (valid)
            cout << cost << '\n';
        else
            cout << "IMPOSSIBLE\n";
    }
}