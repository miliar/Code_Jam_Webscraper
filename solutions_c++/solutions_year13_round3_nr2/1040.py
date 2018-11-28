#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double>vd;
typedef vector<string> vs;
typedef vector<vi>vvi;
typedef map<string,int> msi;
typedef map<int,int>mii;
typedef map<pii,int>mpi;

#define pb push_back
#define MP make_pair
#define popb pop_back
#define all(a) a.begin(), a.end()
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
#define SZ(a) ( (int)a.size() )
#define mem(a, b) memset(a, b, sizeof(a))

#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (i=p; i<k;i++)

#define COPY(c,r)   memcpy(c,r,sizeof(r))
#define popcount(i) __builtin_popcount(i)
#define fs first
#define sc second

/// Moves ///
int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
char dir[] = {'E', 'N', 'W', 'S'};
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[] = {-2, 2, -1, 1, -1, 1};int dy[] = {0, 0, 1, 1, -1, -1}; //Hexagonal Moves

/// Cycles ///
//#define cycl0 0
//#define cycl1 1
//#define cycl5 5
//#define cycl6 6
//int cycl2[] = {1, 2, 4, 8, 6};
//int cycl3[] = {1, 3, 9, 7, 1};
//int cycl4[] = {1, 4, 6};
//int cycl7[] = {1, 7, 9, 3, 1};
//int cycl8[] = {1, 8, 4, 2, 6};
//int cycl9[] = {1, 9, 1};

#define INF 1<<30

struct data
{
    ll x, y;
    string s;
    data(ll x=0, ll y=0, string s="")
    {
        this->x = x;
        this->y = y;
        this->s = s;
    }
};

map<pii, bool>col;
int X, Y;

string bfs(int x, int y, string s);

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;

    cin>>t;
    for (int cas=1; cas<=t; cas++)
    {
        cin>>X>>Y;
        col.clear();
        string res = bfs(0, 0, string(""));
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
	return 0;
}

string bfs(int x, int y, string s)
{
    queue<data>q;

    col[MP(x, y)] = 1;
    q.push(data(x, y, s));

    while(!q.empty())
    {
        data t = q.front(); q.pop();

///        int dx[]={1,0,-1,0};int dy[]={0,1,0,-1};
        /// ENWS
        for (int i=0; i<4; i++)
        {
            ll nx = t.x+(dx[i]*(SZ(t.s)+1)), ny = t.y+(dy[i]*(SZ(t.s)+1));
            string ns = t.s+dir[i];

            if (nx == X && ny == Y) return ns;
            if (col.find(MP(nx, ny))==col.end())
            {
                col[MP(nx, ny)] = 1;
                q.push(data(nx, ny, ns));
            }
        }
    }
    return s;
}
