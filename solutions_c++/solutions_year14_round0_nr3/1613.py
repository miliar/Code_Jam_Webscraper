#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <map>
using namespace std;

const int Wall = -2;
const int Mine = -1;
const int Dot  = -4;
const int Check = -3;


void print_grid(vector<vector<int> >& grid, bool withWalls = false)
{
    int si = 0;
    if (withWalls)
        si = -1;

    for(int i=1+si; i<grid.size()-1-si;++i)
    {
        for(int j=1+si; j<grid[i].size()-1-si; ++j)
        {
            if (grid[i][j] == Mine)
            {
                cout << "*";
            }
            else if (grid[i][j] == Dot)
            {
                cout << ".";
            }
            else if (grid[i][j] == Check)
            {
                cout << "c";
            }
            else if (grid[i][j] == Wall)
            {
                cout << "#";
            }
            else
            {
                cout << grid[i][j];
            }
        }
        cout << endl;
    }
}


void init_pop_grid(int R, int C, int M, vector<vector<int> >& grid)
{
    grid.resize(R+2);
    int mines_remained = M;
    for(int i=0; i<R+2;++i)
    {
        grid[i].resize(C+2);
        grid[i].assign(C+2,0);
        if (i==0 || i==R+1)
        {
            continue;
        }
        for(int j=1;j<=C;++j)
        {
            if (mines_remained>0)
            {
                grid[i][j] = -1;
                --mines_remained;
            }
        }
    }
}

bool make_cell_perfect(vector<vector<int> >& grid_, int &marked_, int r, int c, int ncells, int M)
{
    vector<vector<int> > grid = grid_;
    int marked = marked_;
   
    vector<pair<int, int> > justOpenedCells;
    for(int i=r-1; i<=r+1; ++i)
    {
        for(int j=c-1; j<=c+1; ++j)
        {
            if (i==r && j==c)
            {
                continue;
            }
            if ( grid[i][j] != Wall && grid[i][j] != Dot)
            {
                grid[i][j] = Dot;
                ++marked;
                justOpenedCells.push_back(make_pair(i,j));
            }
        }
    }
    if ( marked + M == ncells)
    {
        grid_ = grid;
        marked_ = marked;
        return true;
    }
    else if ( marked + M > ncells)
    {
        return false;
    }

    for(int i=0; i<justOpenedCells.size();++i)
    {
        bool succ = make_cell_perfect(grid, marked, justOpenedCells[i].first, justOpenedCells[i].second, ncells, M);
        if (succ)
        {
            grid_ = grid;
            marked_ = marked;
            return true;
        }
    }
        
    return false;
}

bool fill_blanks(int M,  vector<vector<int> >& grid, int ncells)
{
    int perfect = 1;
    grid[1][1] = Dot;
    if ( perfect + M == ncells)
    {
        return true;
    }
    else if ( perfect + M > ncells )
    {
        return false;
    }

    return make_cell_perfect(grid, perfect, 1, 1, ncells, M); 
}



void init_pop_grid_empty(int R, int C, vector<vector<int> >& grid)
{
    grid.resize(R+2);
    for(int i=0; i<R+2;++i)
    {
        grid[i].resize(C+2);
        grid[i].assign(C+2, -1);
    }

    grid[0].assign(C+2, Wall);
    grid[R+1].assign(C+2, Wall);
    for(int i=1; i<R+2;++i)
    {
        grid[i][0] = Wall;
        grid[i][C+1] = Wall;
    }
}

bool fill_mines(int M, vector<vector<int> >& grid)
{
    bool canFill = true;
    int mines_remained = M;
    int R = grid.size()-2;
    int C = grid[0].size() -2;
    for(int i=0; i<R+2;++i)
    {
        if (i==0 || i==R+1)
        {
            continue;
        }
        for(int j=1;j<=C;++j)
        {
            if (mines_remained>0)
            {
                if (grid[i][j] == 0)
                {
                    grid[i][j] = -1;
                    --mines_remained;
                }
            }
            else
            {
                if (grid[i][j] == 0)
                {
                    grid[i][j] = -2;
                }
            }
        }
    }
    if (mines_remained==0)
    {
        return true;
    }
    else 
    {
        return false;
    }
}


void calc_num_mines_from_final(vector<vector<int> >& grid)
{
    for(int i=1; i<grid.size()-1;++i)
    {
        for(int j=1; j<grid[i].size()-1; ++j)
        {
            if (grid[i][j] == -1)
                continue;
            int nmines = 0;
            if (grid[i-1][j-1] == -1)
                ++nmines;
            if (grid[i-1][j] == -1)
                ++nmines;
            if (grid[i-1][j+1] == -1)
                ++nmines;
            if (grid[i][j-1] == -1)
                ++nmines;
            if (grid[i][j+1] == -1)
                ++nmines;
            if (grid[i+1][j-1] == -1)
                ++nmines;
            if (grid[i+1][j] == -1)
                ++nmines;
            if (grid[i+1][j+1] == -1)
                ++nmines;
            grid[i][j] = nmines;
        }
    }
}
void calc_num_mines(vector<vector<int> >& grid)
{
    for(int i=1; i<grid.size()-1;++i)
    {
        for(int j=1; j<grid[i].size()-1; ++j)
        {
            if (grid[i][j] < 0)
                continue;
            int nmines = 0;
            if (grid[i-1][j-1] == -1)
                ++nmines;
            if (grid[i-1][j] == -1)
                ++nmines;
            if (grid[i-1][j+1] == -1)
                ++nmines;
            if (grid[i][j-1] == -1)
                ++nmines;
            if (grid[i][j+1] == -1)
                ++nmines;
            if (grid[i+1][j-1] == -1)
                ++nmines;
            if (grid[i+1][j] == -1)
                ++nmines;
            if (grid[i+1][j+1] == -1)
                ++nmines;
            grid[i][j] = nmines;
        }
    }
}

bool select_click_pos(vector<vector<int> >& grid)
{
    bool solvable = false;
    for(int i=1; i<grid.size()-1;++i)
    {
        for(int j=1; j<grid[i].size()-1; ++j)
        {
            if (grid[i][j] == -1)
                continue;
            else if (grid[i][j] == 0 && solvable == false)
            {
                grid[i][j] = -3;
                solvable = true;
            }
            else 
            {
                grid[i][j] = -2;
            }
        }
    }
    return solvable;
}

int main()
{

    int T;
    cin >> T;

    for(int icase=0; icase < T; ++icase)
    {
        vector<vector<int> > grid;
        int R, C, M;
        cin >> R >> C >> M;
        
        //init_pop_grid(R, C, M, grid);
        init_pop_grid_empty(R, C, grid);

        cout << "Case #" << icase+1 << ":" << endl;

//        cout << R << " " << C << " " << M << endl;

        bool solvable = fill_blanks(M, grid, R*C);
        

//        bool solvable = fill_mines(M, grid);


        if (solvable)
        {
            grid[1][1] = Check;
            print_grid(grid, false);
        }
        else
        {
            cout << "Impossible" << endl;
        }

    }

}
