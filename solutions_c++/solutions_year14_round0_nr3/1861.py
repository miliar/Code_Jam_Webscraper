#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Grid
{
    public:
    Grid(int r, int c)
    {
        _cells.resize(r);
        for(auto& v : _cells)
            v.resize(c);

        for(size_t i=0 ; i<_cells.size() ; ++i)
            for(size_t j=0 ; j<_cells[i].size() ; ++j)
        {
            _cells[i][j] = 0;
        }

        _cells[0][0] = 1;
        _mines = r*c-1;
        Next n = {0,0,0};
        computeWeight(n);
        _nextStep.push_back(n);
    }

    struct Next
    {
        int x,y;
        int weight;
    };


    void click(size_t indexNext)
    {
        Next n=_nextStep[indexNext];
        _cells[n.x][n.y]=2;
        _mines -= n.weight;

        std::swap(_nextStep[indexNext], _nextStep[_nextStep.size()-1]);
        _nextStep.pop_back();

        for(int i=n.x-1 ; i<= n.x+1 ; ++i)
            for(int j=n.y-1 ; j<= n.y+1 ; ++j)
        {
            if(i<0 || j<0 || i >= (int)_cells.size() || j >= (int)_cells[0].size())
                continue;

            if(_cells[i][j]==0)
            {
                _cells[i][j]=1;
                _nextStep.push_back({i,j,0});
            }
        }

        for(auto& n : _nextStep)
            computeWeight(n);

        //filterNextStep();
        sortStep();
    }

    void filterNextStep()
    {
        vector<Next> tmp = std::move(_nextStep);
        for(size_t i=0 ; i<tmp.size() ; ++i)
        {
            if(tmp[i].weight <= 2)
                _nextStep.push_back(tmp[i]);
        }
    }

    void computeWeight(Next& n)
    {
        n.weight=0;
        for(int i=n.x-1 ; i<= n.x+1 ; ++i)
            for(int j=n.y-1 ; j<= n.y+1 ; ++j)
        {
            if(i<0 || j<0 || i >= (int)_cells.size() || j >= (int)_cells[0].size())
                continue;

            if(_cells[i][j]==0)
                n.weight++;
        }
    }

    void sortStep()
    {
        std::sort(_nextStep.begin(), _nextStep.end(), [](const Next& a, const Next& b){ return a.weight<b.weight; });
    }

    void print()
    {
        for(size_t i=0 ; i<_cells.size() ; ++i)
        {
            for(size_t j=0 ; j<_cells[i].size() ; ++j)
            {
                if(i==0 && j==0)
                    cout << "c";
                else
                {
                    switch(_cells[i][j])
                    {
                        case 0: cout << "*"; break;
                        case 1:
                        case 2: cout << "."; break;
                    }
                }
            }
            cout << endl;
        }
    }


    vector<Next> _nextStep;
    int _mines;
    vector<vector<int>> _cells;
};

void rec(Grid& grid, int mine)
{
    for(size_t i=0 ; i<grid._nextStep.size() ; i++)
    {
        Grid tmp=grid;
        tmp.click(i);
        if(tmp._mines == mine)
            throw tmp;
        else if(tmp._mines > mine)
        {
            rec(tmp, mine);
        }
    }
}

int main()
{
    int nb;
    cin >> nb;
    for(int i=0 ; i<nb ; i++)
    {
        cout << "Case #"<<i+1<<":"<<endl;
        int x,y,m;
        cin >> x >> y >> m;
        Grid g(x,y);
        bool findsol=false;
        try
        {
            if(g._mines == m)
                throw g;
            else
                rec(g, m);
        }
        catch(Grid solution)
        {
            findsol=true;
            solution.print();
        }
        if(!findsol)
            cout << "Impossible" << endl;
    }
}
