#include <iostream>
#include <cstdio>
#include <string>
#include <sstream> 
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <ctime>
using namespace std;
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define vi vector<int>
#define SZ(x) ((int)(x.size()))
#define fi first
#define se second
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define DBG cerr << "debug here" << endl;
#define DBGV(vari) cerr << #vari<< " = "<< (vari) <<endl;

typedef long long ll;
typedef double fl;

typedef struct Elem
{
    vi v;
    int steps;
} Elem;

int main()
{
    int T;
    cin >> T;
    REP(t, 1, T)
    {
        set<vi> visited;
        int d;
        cin >> d;
        Elem init;
        FOR(i, d)
        {
            int v;
            cin >> v;
            init.v.pb(v);
            sort(ALL(init.v));
        }
        queue<Elem> Q;
        init.steps = 0;
        Q.push(init);
        while(!Q.empty())
        {
            Elem e = Q.front();
            Q.pop();
            if(visited.find(e.v) != visited.end()) continue;
            visited.insert(e.v);
            if(e.v.empty())
            {
                cout << "Case #" << t << ": " << e.steps << endl;
                break;
            }
            Elem reduce;            
            FOR(i, e.v.size())
            {
                int v = e.v[i] - 1;
                if(v > 0)
                {
                    reduce.v.pb(v);
                }
            }
            reduce.steps = e.steps + 1;
            Q.push(reduce);
            FOR(i, e.v.size())
            {
                int v = e.v[i];
                if(v == 1) continue;
                REP(j, 1, v - 1)
                {
                    Elem move;
                    move.v = e.v;
                    move.v[i] = move.v[i] - j;
                    move.v.pb(j);
                    sort(ALL(move.v));
                    move.steps = e.steps + 1;
                    Q.push(move);
                }
            }
        }
    }

    return 0;
}
