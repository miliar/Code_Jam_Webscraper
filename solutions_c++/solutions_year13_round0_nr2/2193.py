#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

const int MAXH = 100;

pair<int,int> findmin(const vector<vector<int>>& lawn)
{
    pair<int,int> minp(0, 0);
    for(int i=0;i<lawn.size();++i)
    {
        for(int j=0;j<lawn[i].size();++j)
        {
            if (lawn[i][j] < lawn[minp.first][minp.second])
            {
                minp = make_pair(i,j);
            }
        }
    }
    
    return minp;
}

bool tryuncut(vector<vector<int>>& lawn, const pair<int,int>& c)
{
    bool canuncut = false;
    int minv = lawn[c.first][c.second];
    
    bool canuncutrow = true;
    for (int j=0;j<lawn[c.first].size();++j)
    {
        if(lawn[c.first][j] > minv && lawn[c.first][j] <= MAXH)
        {
            canuncutrow = false;
            break;
        }
    }
    
    if (canuncutrow)
    {
    for (int j=0;j<lawn[c.first].size();++j)
    {
        lawn[c.first][j] = MAXH + 1;
    }
    }
    
    bool canuncutcol = true;
    for (int i=0;i<lawn.size();++i)
    {
        if(lawn[i][c.second] > minv && lawn[i][c.second] <= MAXH)
        {
            canuncutcol = false;
            break;
        }
    }
    
    if (canuncutcol)
    {
    for (int i=0;i<lawn.size();++i)
    {
        lawn[i][c.second] = MAXH + 1;
    }
    }
    
    return canuncutrow || canuncutcol;
}

bool cancut(vector<vector<int>>& lawn)
{
    while(true)
    {
        auto minp = findmin(lawn);
        if(lawn[minp.first][minp.second] > MAXH)
        {
            break;
        }
        
        if(!tryuncut(lawn, minp))
        {
            return false;
        }
    }
    
    return true;
}

int main()
{
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
        int m,n;
        cin >> m >> n;
        vector<vector<int>> lawn(m, vector<int>(n));
        for(auto& v : lawn)
        {
            for(auto& x : v)
            {
                cin >> x;
            }
        }
        
        cout << "Case #"<< lp << ": " << (cancut(lawn) ? "YES" : "NO") << "\n"; 
    }
    
    return 0;
}