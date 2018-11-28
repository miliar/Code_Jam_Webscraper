#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(auto i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(auto i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

const int UP = 0;
const int LEFT = 1;
const int DOWN = 2;
const int RIGHT = 3;

const int dirDx[4] = {-1,0,1,0};
const int dirDy[4] = {0,-1,0,1};
const int dirInv[4] = {DOWN, RIGHT, UP, LEFT};

const int dx[2][4] = {{0,-1,0,1}, 
                      {0, 1,0,-1} 
                      };

const int dy[2][4] = {{-1, 0, 1,0}, 
                      { 1, 0,-1,0} 
                     };

const int moveND[2][4] = {{3, 2, 1,0}, 
                      {1, 0, 3,2} 
                     };

bool pairs[512][512];

char result[128][128];

int R,C;

void encode(int source, int &xsource, int &ysource, int &dsource)
{
    if (source < C)
    {
        xsource = 0;
        ysource = source;
        dsource = UP;
    }
    else if (source < C+R)
    {
        xsource = source - C;
        ysource = C-1;
        dsource = RIGHT;
    }
    else if (source < C+R+C)
    {
        xsource = R-1;
        ysource = C-1-(source - (C+R));
        dsource = DOWN;
    }
    else
    {
        xsource = R-1 - (source - (2*C+R));
        ysource = 0;
        dsource = LEFT;
    }
}

bool go(int source, int destination)
{
    int xsource;
    int ysource;
    int dsource;
    encode(source, xsource, ysource, dsource);
    int xdest, ydest, ddest;
    encode(destination, xdest, ydest, ddest);
    xdest += dirDx[ddest];
    ydest += dirDy[ddest];
    ddest = dirInv[ddest];
    
    //cout << source << " " << xsource << " " << ysource << " " << dsource << endl;
    //cout << destination << " " << xdest << " " << ydest << " " << ddest << endl;
    
    deque<int> q;
    q.push_back(xsource);
    q.push_back(ysource);
    q.push_back(dsource);
    map<tuple<int,int,int> , int> distance;
    map<tuple<int,int,int> , pair<tuple<int,int,int>, int> > prev;
    distance[tuple<int,int,int>(xsource, ysource, dsource)] = 0;
    while (!q.empty())
    {
        int x,y,d;
        x = q.front(); q.pop_front();
        y = q.front(); q.pop_front();
        d = q.front(); q.pop_front();
        tuple<int,int,int> currentState{x,y,d};
        #define rangeOk(x,y) 0 <= x && x < R && 0 <= y && y < C
        if (x == xdest && y == ydest && d == ddest)
        {
            while (esta(currentState, prev))
            {
                auto par = prev[currentState];
                currentState = par.first;
                int symbol = par.second;
                x = get<0>(currentState);
                y = get<1>(currentState);
                assert(rangeOk(x,y));
                if (result[x][y] >= 0)
                    assert(symbol == result[x][y]);
                result[x][y] = symbol;
            }
            return true;
        }
        int currentDistance = distance[currentState];
        if (rangeOk(x,y))
        {
            forn(symbol, 2)
            if (result[x][y] < 0 || result[x][y] == symbol)
            {
                const int nx = x + dx[symbol][d];
                const int ny = y + dy[symbol][d];
                const int nd = moveND[symbol][d];
                const int newDistance = currentDistance + (result[x][y] < 0);
                tuple<int,int,int> est{nx,ny,nd};
                if (!esta(est, distance) || newDistance < distance[est])
                {
                    distance[est] = newDistance;
                    prev[est] = make_pair(currentState, symbol);
                    if (result[x][y] < 0)
                    {
                        q.push_back(nx);
                        q.push_back(ny);
                        q.push_back(nd);
                    }
                    else
                    {
                        q.push_front(nd);
                        q.push_front(ny);
                        q.push_front(nx);
                    }
                }
            }
        }
    }
    return false;
}

int main()
{
    int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        cin >> R >> C;
        int N = 2*(R+C);
        forn(i,N)
        forn(j,N)
            pairs[i][j] = false;
        forn(i,N/2)
        {
            int x,y; cin >> x >> y;
            x--; y--;
            assert(0 <= x);
            assert(x < N);
            assert(0 <= y);
            assert(y < N);
            pairs[x][y] = true;
            pairs[y][x] = true;
        }
        vector<int> v(N);
        forn(i,N) v[i] = i;
        
        forn(i,R)
        forn(j,C)
            result[i][j] = -1;
        
        bool possible = true;
        
        forn(steps, N/2)
        {
            forn(i,v.size())
            {
                int next = (i+1)%v.size();
                if (pairs[v[i]][v[next]])
                {
                    const int source = v[i];
                    const int destination = v[next];
                    const int minIndex = min(i, next);
                    const int maxIndex = max(i, next);
                    v.erase(v.begin() + maxIndex);
                    v.erase(v.begin() + minIndex);
                    if (!go(source, destination))
                        break;
                    goto todoBienPapa;
                }
            }
            possible = false;
            break;
todoBienPapa:;
        }
        
		cout << "Case #" << caso + 1 << ":\n";
        
        if (possible)
        {
            forn(i,R)
            {
                forn(j,C)
                if (result[i][j] >= 0)
                    cout << "/\\"[(int)result[i][j]];
                else
                    cout << '/';
                cout << "\n";
            }
        }
        else
            cout << "IMPOSSIBLE\n";
	}
	return 0;
}
