#include <iostream> 
#include <vector> 
#include <queue> 
#include <string> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <iomanip> 
#include <sstream> 
#include <algorithm> 
#include <map> 
#include <set> 
#include <fstream>
using namespace std;

typedef pair<int, int> PI;

int x, y;

int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};
char dir[] = {'W', 'E', 'N', 'S'};

struct state {
   int posX;
   int posY;
   int moves;    
   
   state(int posX, int posY, int moves) : posX(posX), posY(posY), moves(moves) { }
   bool operator < (const state& o) const
   {
       if (posX != o.posX) return posX < o.posX;
       if (posY != o.posY) return posY < o.posY;
       return moves < o.moves; 
   }
};

queue<state> Q;
set<state> vis;

map<state, char> prev;

void push(char dir, int nextX, int nextY, int nextMoves)
{
    state next(nextX, nextY, nextMoves);          
    if (vis.count(next)) return;
    
    Q.push(next); 
    vis.insert(next);
    prev[next] = dir;
}

void solve()
{
    while (!Q.empty()) Q.pop();
    
    vis.clear();
    prev.clear();
    
    state beg(0, 0, 0);     
    Q.push(beg); 
    vis.insert(beg);
    prev[beg] = '#';
    
    while (!Q.empty())
    {
        state cur = Q.front(); Q.pop();
        if (cur.moves > 500) continue;
        //if (abs(cur.posX) > 1000 || abs(cur.posY) > 1000) continue; 
        
        if (cur.posX == x && cur.posY == y)
        {
            string ans = "";         
            state temp = cur;
            
            while (prev[temp] != '#')
            {
               ans += prev[temp]; 
               
               int oldX = temp.posX;
               int oldY = temp.posY;
               if (prev[temp] == 'N')
                  oldY -= temp.moves;
               else
               if (prev[temp] == 'S')
                  oldY += temp.moves;
               else if (prev[temp] == 'W')
                  oldX += temp.moves;
               else
                  oldX -= temp.moves;
               
               temp = state(oldX, oldY, temp.moves - 1);
            }
            
            reverse(ans.begin(), ans.end());
            cout << ans << endl;
            break;
        }
        
        for (int i = 0; i < 4; i++)
        {
            int nextMoves = cur.moves + 1;            
            int nextX = cur.posX + (dx[i] * nextMoves);
            int nextY = cur.posY + (dy[i] * nextMoves);
            
            push(dir[i], nextX, nextY, nextMoves);
        }  
    }
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> x >> y;
        
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}
