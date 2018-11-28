#include<algorithm>
#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<sstream>
#include<queue>
#include<vector>

using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

vector<string> grid;
int r,c;

string convert(int t)
{
    if(t == -1)
        return "IMPOSSIBLE";
    ostringstream oss;
    oss.str("");
    oss.clear();
    oss << t;
    return oss.str();
}

bool encuentroAlguna(int i, int j)
{
    forn(ii,r)
    {
        if(ii!=i && grid[ii][j] != '.')
            return true;
    }
    forn(jj,c)
    {
        if(jj!=j && grid[i][jj] != '.')
            return true;
    }
    return false;
}

int calc()
{
    int res = 0;
    forn(i,r)
    forn(j,c)
    {
        if(grid[i][j] == '^')
        {
            int i2 = i-1;
            bool b = false;
            while(i2>=0)
            {
                if(grid[i2][j] != '.')
                {
                    b = true;
                    break;
                }
                i2--;
            }
            if(b == false)
            {
                res++;
                if(encuentroAlguna(i,j)==false)
                    return -1;
            }
        }
        if(grid[i][j] == 'v')
        {
            int i2 = i+1;
            bool b = false;
            while(i2<r)
            {
                if(grid[i2][j] != '.')
                {
                    b = true;
                    break;
                }
                i2++;
            }
            if(b == false)
            {
                res++;
                if(encuentroAlguna(i,j)==false)
                    return -1;
            }
        }
        if(grid[i][j] == '<')
        {
            int j2 = j-1;
            bool b = false;
            while(j2>=0)
            {
                if(grid[i][j2] != '.')
                {
                    b = true;
                    break;
                }
                j2--;
            }
            if(b == false)
            {
                res++;
                if(encuentroAlguna(i,j)==false)
                    return -1;
            }
        }
        if(grid[i][j] == '>')
        {
            int j2 = j+1;
            bool b = false;
            while(j2<c)
            {
                if(grid[i][j2] != '.')
                {
                    b = true;
                    break;
                }
                j2++;
            }
            if(b == false)
            {
                res++;
                if(encuentroAlguna(i,j)==false)
                    return -1;
            }
        }
    }
    return res;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int casos;
    cin >> casos;
    for(int casito = 1; casito <= casos; casito++)
    {
        cin >> r >> c;
        grid.resize(r);
        forn(i,r)
            cin >> grid[i];
        cout << "Case #"<<casito<<": " << convert(calc()) << endl;
    }
}
