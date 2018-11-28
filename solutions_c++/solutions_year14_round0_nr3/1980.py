#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool MaySpread(const int& row, const int& column, const int& rowSize, const int& columnSize, const vector<int>& isMine)
{
    for (int rc = row - 1; rc < row + 2; ++rc)
    {
        for (int cc = column-1; cc < column+2; ++cc)
        {
            if (rc >= 0 && cc >= 0 && rc < rowSize && cc < columnSize && isMine[cc * rowSize + rc])
            {
                return false;
            }
        }
    }
    
    return true;
}

void SpreadOut(const vector<int>& isMine, vector<bool>& possible, int row, int column, int rowSize, int columnSize)
{
    possible[column * rowSize + row] = true;
    
    if (MaySpread(row, column, rowSize, columnSize, isMine))
    {
        for (int rc = row - 1; rc < row + 2; ++rc)
        {
            for (int cc = column-1; cc < column+2; ++cc)
            {
                if (rc >= 0 && cc >= 0 && rc < rowSize && cc < columnSize && !possible[cc * rowSize + rc])
                    SpreadOut(isMine, possible, rc, cc, rowSize, columnSize);
            }
        }
    }
}


bool TryCombination(const vector<int>& isMine, int rowSize, int columnSize, int& toClick)
{
    vector<bool> possible(isMine.size(), false);
    
    bool spreadOut = false;
    
    for (int i = 0; i < isMine.size(); ++i)
    {
        if (!isMine[i])
        {
            bool willSpread(true);
            
            int row = i % rowSize;
            int column = i / rowSize;
            
            
            if (MaySpread(row, column, rowSize, columnSize, isMine))
            {
                possible[i] = true;
                
                spreadOut = true;
                
                for (int rc = row - 1; rc < row + 2; ++rc)
                {
                    for (int cc = column-1; cc < column+2; ++cc)
                    {
                        if (rc >= 0 && cc >= 0 && rc < rowSize && cc < columnSize && !possible[cc * rowSize + rc])
                            SpreadOut(isMine, possible, rc, cc, rowSize, columnSize);
                    }
                }
                
                toClick = i;
            }
            
            break;
        }
    }
    
    bool singleNonSpread(true);
    
    for (int i = 0; i < isMine.size(); ++i)
    {
        if (!isMine[i] && !possible[i])
        {
            if (!spreadOut && singleNonSpread)
            {
                toClick = i;
                singleNonSpread = false;
            }
            
            else
            {
                toClick = -1;
                return false;
            }
        }
    }
    
    return true;
}



int main()
{
    vector<int> combinations;
    
    int toClick, rowSize, columnSize, T, numMines;
    
    scanf("%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d %d %d", &columnSize, &rowSize, &numMines);
        
        combinations.resize(columnSize * rowSize);
        
        for (int i = 0; i < combinations.size(); ++i)
        {
            if (i >= combinations.size() - numMines)
                combinations[i] = 1;
            else
                combinations[i] = 0;
        }
        
        toClick = -1;
        
        printf("Case #%d:\n", t);
        
        do {
            if (TryCombination(combinations, rowSize, columnSize, toClick))
            {
                for (int c = 0; c < columnSize; ++c)
                {
                    for (int r = 0; r < rowSize; ++r)
                    {
                        if (combinations[c * rowSize + r])
                            printf("*");
                        
                        else if (toClick == c * rowSize + r)
                            printf("c");
                        else
                            printf(".");
                    }
                    printf("\n");
                }
                break;
            }
        } while ( std::next_permutation(combinations.begin(),combinations.end()) );
        
        if (toClick == -1)
            printf("Impossible\n");
    }
}