#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1 << 30;
const double EPS = 1e-8;
int w, h, b;
vector<pair<pii, pii> > v;

int dist(int x, int y)
{
    int dx=max(v[y].fi.fi-v[x].se.fi, v[x].fi.fi-v[y].se.fi);
    int dy=max(v[y].fi.se-v[x].se.se, v[x].fi.se-v[y].se.se);
    dx=max(0,dx-1);
    dy=max(0,dy-1);
    return max(dx,dy);
    /*if(v[x].se.fi<=v[y].fi.fi) // x na lewo
    {

    }
    else if(v[x].fi.fi>=v[y].se.fi) // x na lewo
    {

    }
    else // pokrycie na x
    {

    }*/
}

void solve(int num)
{
    cin>>w>>h>>b;
    v.resize(b+2);
    v[0]=mp(mp(-1,0), mp(-1,h));
    v[b+1]=mp(mp(w,0),mp(w,h));
    for(int i=1; i<=b; i++)
    {
        cin>>v[i].fi.fi>>v[i].fi.se>>v[i].se.fi>>v[i].se.se;
    }
    vi d(b+5,INF);
    d[0]=0;
    priority_queue<pii, vector<pii>, greater<pii> > pq;
    pq.push(mp(0, 0));
    vi bylo(b+5,0);
    while(pq.size())
    {
        int cur=pq.top().se, dd=pq.top().fi;
        pq.pop();
        if(bylo[cur]) continue;
        bylo[cur]=1;
        for(int i=1; i<=b+1; i++)
        {
            if(bylo[i]) continue;
            int meh=dist(cur, i);
            if(d[cur]+meh<d[i])
            {
                d[i]=d[cur]+meh;
                pq.push(mp(d[i],i));
            }
        }
    }
    /*cout<<endl;
    for(int i=0; i<=b+1; i++)
    {
        for(int j=0; j<=b+1; j++) cout<<dist(i,j)<<" ";
        cout<<endl;
    }*/
    cout<<"Case #"<<num<<": "<<d[b+1]<<"\n";


}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}

