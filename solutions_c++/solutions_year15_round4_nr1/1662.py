/************************************************************
 * Author: Priyanshu Singh
 * Handle: tgamerz
 */

#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>
#include <iomanip>   
#include <iostream>  
#include <sstream> 
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <bitset>

using namespace std;
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%f",&n)
#define slf(n)                      scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9

// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define F                           first
#define S                           second

// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

#define DEBUG

// debugging
#ifdef DEBUG
#define trace1(x)                    cerr << #x << ": " << x << endl;
#define trace2(x, y)                 cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)              cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)           cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)        cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f)     cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#else
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
#endif

//dirextion
const int fx[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
const int fxx[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};

// datatypes
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define us unsigned short

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair< pii, int> piii;
typedef vector< piii > vpiii;
typedef pair<int, bool> pib;
typedef vector< pii > vpii;
typedef vector< pib > vpib;

const int MAXN = 110;
bool vis[MAXN][MAXN];
char grid[MAXN][MAXN];
int memo[MAXN][MAXN];

const int UP = 0;
const int DOWN = 1;
const int LEFT = 2;
const int RIGHT = 3;

int T,R,C;

const int getDir(int i,int j){
    if(grid[i][j] == '^')return UP;
    else if(grid[i][j] == 'v')return DOWN;
    else if(grid[i][j] == '<')return LEFT;
    else if(grid[i][j] == '>')return RIGHT;
    else {
        printf("SCREWED\n");
        trace2(i, j)
    }
    return -1;
}

inline bool isarrow(int i,int j){
    return (grid[i][j] == '^' || grid[i][j] == 'v' || grid[i][j] == '<' || grid[i][j] == '>');
}

int DFS(int i, int j){
    //trace3(i, j,1)
    if(vis[i][j])return 0;
    int x=i,y=j;
    vis[i][j] = true;
    if(getDir(i,j) == UP){
        x--;
        for(; x < R && x >= 0; x--){
            if(isarrow(x, y))return DFS(x, y);
        }
    }else if(getDir(i, j) == DOWN){
        x++;
        for(; x < R && x >=0; x++){
            if(isarrow(x, y))return DFS(x, y);
        }
    }else if(getDir(i, j) == RIGHT){
        y++;
        for(; y < C && y >=0; y++){
            if(isarrow(x, y))return DFS(x,y);
        }
    }else if(getDir(i, j) == LEFT){
        y--;
        for(; y < C && y>=0; y--){
            if(isarrow(x, y))return DFS(x, y);
        }
    }
    x=i;x=j;
    forall(d, 0, 4){
        if(getDir(i, j) != d){
            x=i;y=j;
            if(d==UP){
                x--;
                for(; x < R && x >= 0; x--){
                    if(isarrow(x, y)){
                        int a = DFS(x, y);
                        return (a != -1)? a + 1: -1;
                    }
                }        
            }else if(d==DOWN){
                x++;
                for(; x < R && x >=0; x++){
                    if(isarrow(x, y)){
                        int a = DFS(x, y);
                        return (a != -1)? a + 1: -1;
                    }
                }
            }else if(d==LEFT){
                y--;
                for(; y < C && y>=0; y--){
                    if(isarrow(x, y)){
                        int a = DFS(x, y);
                        return (a != -1)? a + 1: -1;
                    }
                }
            }else if(d==RIGHT){
                y++;
                for(; y < C && y >=0; y++){
                    if(isarrow(x, y)){
                        int a = DFS(x, y);
                        return (a != -1)? a + 1: -1;
                    }
                }
            }
        }
    }
    return -1;
}

int main(){
    s(T);
    forall(t, 1, T+1){
        s(R);s(C);
        forall(i, 0, R)ss(grid[i]);
        vpii arr;
        forall(i, 0, R){
            forall(j, 0, C){
                if(isarrow(i, j)){
                    arr.pb(mp(i,j));
                }
            }
        }
        fill(vis,0);
        forall(i, 0, R)forall(j, 0, C)memo[i][j] = -1000;
        int ans = 0;
        bool flag = true;
        forall(a, 0, arr.size()){
            int x = arr[a].F;
            int y = arr[a].S;
            if(!vis[x][y]){
                int a = DFS(x, y);
                if(a == -1){
                    flag = false;
                    break;
                }
                else ans += a;
            }
        }
        if(flag){
            printf("Case #%d: %d\n",t,ans);
        }else{
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
    }
}